"""
Data Visualization Script
انواع نمودارهای آماری:
- Box Plot (نمودار جعبه‌ای)
- Histogram (هیستوگرام)
- KDE (Kernel Density Estimation)
- ECDF (Empirical Cumulative Distribution Function)
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# تنظیم استایل زیبا برای نمودارها
sns.set_theme(style="whitegrid", palette="tab10", rc={'figure.figsize':(10,6)})
plt.rcParams['font.family'] = 'sans-serif'

def plot_histogram(data, column, bins=30, kde=True, title=None):
    """
    رسم هیستوگرام با قابلیت افزودن منحنی KDE
    
    هیستوگرام: توزیع فراوانی داده‌ها را نشان می‌دهد
    KDE: تخمین چگالی هسته - نسخه صاف‌شده هیستوگرام
    """
    fig, ax = plt.subplots(figsize=(10, 6))
    
    sns.histplot(data=data, x=column, bins=bins, kde=kde, 
                 edgecolor='black', alpha=0.6, ax=ax)
    
    title_text = title or f'توزیع داده‌های {column}'
    ax.set_title(title_text, fontsize=14, fontweight='bold')
    ax.set_xlabel(column, fontsize=12)
    ax.set_ylabel('تعداد (Frequency)', fontsize=12)
    
    # اضافه کردن متن توضیحی
    ax.text(0.02, 0.98, '📊 هیستوگرام: توزیع فراوانی\n📈 KDE: منحنی چگالی',
            transform=ax.transAxes, fontsize=10,
            verticalalignment='top', bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))
    
    plt.tight_layout()
    return fig

def plot_kde(data, column, bw_method='scott'):
    """
    رسم منحنی KDE (Kernel Density Estimation)
    
    KDE: برآورد چگالی هسته - روشی برای تخمین تابع چگالی احتمال
    """
    fig, ax = plt.subplots(figsize=(10, 6))
    
    sns.kdeplot(data=data, x=column, fill=True, alpha=0.6, 
                bw_method=bw_method, linewidth=2, ax=ax)
    
    ax.set_title(f'منحنی چگالی KDE برای {column}', fontsize=14, fontweight='bold')
    ax.set_xlabel(column, fontsize=12)
    ax.set_ylabel('چگالی (Density)', fontsize=12)
    
    ax.text(0.02, 0.98, '🎯 KDE: برآورد تابع چگالی احتمال\nنشان می‌دهد داده‌ها در چه نقاطی متمرکزند',
            transform=ax.transAxes, fontsize=10,
            verticalalignment='top', bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.5))
    
    plt.tight_layout()
    return fig

def plot_ecdf(data, column):
    """
    رسم ECDF (Empirical Cumulative Distribution Function)
    
    ECDF: تابع توزیع تجمعی تجربی
    نشان می‌دهد چند درصد داده‌ها کمتر از یک مقدار خاص هستند
    """
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # محاسبه ECDF
    sorted_data = np.sort(data[column].dropna())
    y_ecdf = np.arange(1, len(sorted_data) + 1) / len(sorted_data)
    
    ax.step(sorted_data, y_ecdf, where='post', linewidth=2, color='steelblue')
    ax.fill_between(sorted_data, y_ecdf, alpha=0.2, color='steelblue')
    
    ax.set_title(f'ECDF برای {column}', fontsize=14, fontweight='bold')
    ax.set_xlabel(column, fontsize=12)
    ax.set_ylabel('توزیع تجمعی (Cumulative Probability)', fontsize=12)
    ax.grid(True, alpha=0.3)
    
    # اضافه کردن خطوط راهنما برای تفسیر ECDF
    median_val = np.median(sorted_data)
    median_percentile = np.searchsorted(sorted_data, median_val) / len(sorted_data)
    ax.axvline(median_val, color='red', linestyle='--', alpha=0.7, label=f'میانه: {median_val:.2f}')
    ax.axhline(median_percentile, color='green', linestyle='--', alpha=0.7, label=f'صدک ۵۰٪: {median_percentile:.2f}')
    ax.legend()
    
    ax.text(0.02, 0.98, '📈 ECDF: درصد داده‌هایی که ≤ یک مقدار خاص هستند\nمثال: در ۵۰٪ داده‌ها مقدار ≤ میانه است',
            transform=ax.transAxes, fontsize=10,
            verticalalignment='top', bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.5))
    
    plt.tight_layout()
    return fig

def plot_boxplot(data, column, show_outliers=True, title=None):
    """
    رسم Box Plot (نمودار جعبه‌ای)
    
    Box Plot: نمایش چارک‌ها، میانه، دامنه و اوتلایرها
    - جعبه: از Q1 تا Q3 (IQR)
    - خط وسط: میانه (Q2)
    - سبیل‌ها: 1.5 * IQR
    - نقاط: اوتلایرها
    """
    fig, ax = plt.subplots(figsize=(10, 6))
    
    box = sns.boxplot(data=data, y=column, ax=ax, showfliers=show_outliers,
                      color='lightblue', linewidth=2)
    
    title_text = title or f'Box Plot برای {column}'
    ax.set_title(title_text, fontsize=14, fontweight='bold')
    ax.set_ylabel(column, fontsize=12)
    
    # محاسبه و نمایش آمار
    Q1 = data[column].quantile(0.25)
    Q2 = data[column].median()
    Q3 = data[column].quantile(0.75)
    IQR = Q3 - Q1
    
    stats_text = f'📊 آمار:\nQ1 (چهارک اول): {Q1:.2f}\nQ2 (میانه): {Q2:.2f}\nQ3 (چهارک سوم): {Q3:.2f}\nIQR: {IQR:.2f}'
    
    ax.text(0.02, 0.98, stats_text, transform=ax.transAxes, fontsize=10,
            verticalalignment='top', bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.7))
    
    plt.tight_layout()
    return fig

def plot_combined_analysis(data, column):
    """
    نمایش ترکیبی از تمام نمودارها در یک صفحه
    """
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    
    # 1. هیستوگرام + KDE
    sns.histplot(data=data, x=column, bins=30, kde=True, ax=axes[0, 0], edgecolor='black')
    axes[0, 0].set_title(f'هیستوگرام + KDE - {column}')
    
    # 2. Box Plot
    sns.boxplot(data=data, y=column, ax=axes[0, 1])
    axes[0, 1].set_title(f'Box Plot - {column}')
    
    # 3. KDE فقط
    sns.kdeplot(data=data, x=column, fill=True, ax=axes[1, 0])
    axes[1, 0].set_title(f'KDE - {column}')
    
    # 4. ECDF
    sorted_data = np.sort(data[column].dropna())
    y_ecdf = np.arange(1, len(sorted_data) + 1) / len(sorted_data)
    axes[1, 1].step(sorted_data, y_ecdf, where='post')
    axes[1, 1].set_title(f'ECDF - {column}')
    axes[1, 1].set_ylabel('Cumulative Probability')
    
    plt.suptitle(f'📊 آنالیز جامع توزیع {column}', fontsize=16, fontweight='bold')
    plt.tight_layout()
    return fig

# ============== مثال روی دیتای مصنوعی ==============
if __name__ == "__main__":
    # ساختن دیتای مصنوعی
    np.random.seed(42)
    
    # دیتای نرمال
    normal_data = np.random.normal(100, 15, 500)
    
    # دیتای اسکیو (چوله)
    skewed_data = np.random.exponential(2, 500) * 30
    
    # دیتای دو مد (bimodal)
    bimodal_data = np.concatenate([
        np.random.normal(50, 10, 300),
        np.random.normal(150, 10, 300)
    ])
    
    df = pd.DataFrame({
        'normal': normal_data,
        'skewed': skewed_data,
        'bimodal': bimodal_data
    })
    
    # بررسی هر ستون
    for col in df.columns:
        print(f"\n{'='*50}")
        print(f"📊 تحلیل ستون: {col}")
        print(f"{'='*50}")
        
        # 1. هیستوگرام
        fig1 = plot_histogram(df, col, title=f'هیستوگرام - {col}')
        plt.savefig(f'../images/histogram_{col}.png')
        plt.show()
        
        # 2. KDE
        fig2 = plot_kde(df, col)
        plt.savefig(f'../images/kde_{col}.png')
        plt.show()
        
        # 3. ECDF
        fig3 = plot_ecdf(df, col)
        plt.savefig(f'../images/ecdf_{col}.png')
        plt.show()
        
        # 4. Box Plot
        fig4 = plot_boxplot(df, col)
        plt.savefig(f'../images/boxplot_{col}.png')
        plt.show()
        
        # 5. ترکیبی
        fig5 = plot_combined_analysis(df, col)
        plt.savefig(f'../images/combined_{col}.png')
        plt.show()
    
    print("\n" + "="*50)
    print("🎉 تمام نمودارها ذخیره شدند!")
    print("="*50)
