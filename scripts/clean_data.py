"""
Data Cleaning Script - Outlier Detection & Removal
روش‌های تشخیص و حذف اوتلایر:
1. روش IQR (Interquartile Range)
2. روش Z-Score
"""

import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns

def detect_outliers_iqr(data, column, multiplier=1.5):
    """
    تشخیص اوتلایر با روش IQR
    
    Parameters:
    -----------
    data : DataFrame
    column : str
        نام ستون مورد نظر
    multiplier : float
        ضریب IQR (معمولاً 1.5)
    
    Returns:
    --------
    mask : Series
        ماسک布尔 برای مشخص کردن اوتلایرها
    """
    Q1 = data[column].quantile(0.25)
    Q3 = data[column].quantile(0.75)
    IQR = Q3 - Q1
    
    lower_bound = Q1 - multiplier * IQR
    upper_bound = Q3 + multiplier * IQR
    
    mask = (data[column] < lower_bound) | (data[column] > upper_bound)
    
    print(f"\n📊 روش IQR برای ستون '{column}':")
    print(f"   Q1 (چهارک اول): {Q1:.2f}")
    print(f"   Q3 (چهارک سوم): {Q3:.2f}")
    print(f"   IQR: {IQR:.2f}")
    print(f"   حد پایین: {lower_bound:.2f}")
    print(f"   حد بالا: {upper_bound:.2f}")
    print(f"   تعداد اوتلایرها: {mask.sum()}")
    
    return mask

def detect_outliers_zscore(data, column, threshold=3):
    """
    تشخیص اوتلایر با روش Z-Score
    
    Parameters:
    -----------
    data : DataFrame
    column : str
        نام ستون مورد نظر
    threshold : int
        آستانه Z-Score (معمولاً 3)
    
    Returns:
    --------
    mask : Series
        ماسک布尔 برای مشخص کردن اوتلایرها
    """
    z_scores = np.abs(stats.zscore(data[column].dropna()))
    mask = np.abs(stats.zscore(data[column])) > threshold
    
    print(f"\n📊 روش Z-Score برای ستون '{column}':")
    print(f"   آستانه: ±{threshold}")
    print(f"   تعداد اوتلایرها: {mask.sum()}")
    
    return mask

def remove_outliers(data, column, method='iqr', multiplier=1.5, threshold=3):
    """
    حذف اوتلایرها از دیتاست
    
    Parameters:
    -----------
    data : DataFrame
    column : str
        نام ستون
    method : str
        'iqr' یا 'zscore'
    
    Returns:
    --------
    data_cleaned : DataFrame
        دیتاست بدون اوتلایر
    """
    if method == 'iqr':
        mask = detect_outliers_iqr(data, column, multiplier)
    elif method == 'zscore':
        mask = detect_outliers_zscore(data, column, threshold)
    else:
        raise ValueError("method must be 'iqr' or 'zscore'")
    
    data_cleaned = data[~mask].copy()
    print(f"\n✅ قبل از حذف: {len(data)} رکورد")
    print(f"✅ بعد از حذف: {len(data_cleaned)} رکورد")
    print(f"✅ حذف شد: {len(data) - len(data_cleaned)} رکورد ({(len(data)-len(data_cleaned))/len(data)*100:.1f}%)")
    
    return data_cleaned

def plot_comparison_before_after(data_before, data_after, column):
    """
    مقایسه قبل و بعد از حذف اوتلایر با Box Plot
    """
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))
    
    # قبل از حذف
    sns.boxplot(y=data_before[column], ax=axes[0], color='lightcoral')
    axes[0].set_title(f'قبل از حذف اوتلایر - {column}')
    axes[0].set_ylabel(column)
    
    # بعد از حذف
    sns.boxplot(y=data_after[column], ax=axes[1], color='lightgreen')
    axes[1].set_title(f'بعد از حذف اوتلایر - {column}')
    axes[1].set_ylabel(column)
    
    plt.tight_layout()
    return fig

# ============== مثال روی دیتای مصنوعی ==============
if __name__ == "__main__":
    # ساختن دیتای مصنوعی با اوتلایر
    np.random.seed(42)
    normal_data = np.random.normal(100, 15, 200)
    outliers = np.array([200, 210, 15, 8, 250, 5])
    data_with_outliers = np.concatenate([normal_data, outliers])
    
    df = pd.DataFrame({
        'value': data_with_outliers,
        'category': np.random.choice(['A', 'B', 'C'], len(data_with_outliers))
    })
    
    print("=" * 50)
    print("🧹 شروع فرآیند تمیز کردن داده")
    print("=" * 50)
    
    # روش IQR
    df_cleaned_iqr = remove_outliers(df, 'value', method='iqr', multiplier=1.5)
    
    # روش Z-Score
    df_cleaned_zscore = remove_outliers(df, 'value', method='zscore', threshold=3)
    
    # مقایسه بصری
    fig = plot_comparison_before_after(df, df_cleaned_iqr, 'value')
    plt.savefig('../images/outlier_comparison.png')
    plt.show()
    
    print("\n" + "=" * 50)
    print("🎉 فرآیند تمیز کردن با موفقیت انجام شد!")
    print("=" * 50)
