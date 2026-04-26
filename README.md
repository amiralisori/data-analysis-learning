# data-analysis-learning
آموزش های مرتبط با علم داده و تحلیل داده 
# 📊 Data Analysis Learning Repository

<div align="center">

![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-2.2.0-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Seaborn](https://img.shields.io/badge/Seaborn-0.13.0-3776AB?style=for-the-badge)
![Matplotlib](https://img.shields.io/badge/Matplotlib-3.8.0-11557c?style=for-the-badge)

</div>

## 🎯 هدف پروژه

یادگیری و پیاده‌سازی مفاهیم اصلی **تحلیل داده** و **داده‌کاوی** با تمرکز بر:
- تمیز کردن داده و تشخیص اوتلایر (IQR & Z-Score)
- ویزوالایزیشن حرفه‌ای با Seaborn و Matplotlib
- درک توزیع داده‌ها با نمودارهای مختلف

## 📈 نمودارهای پیاده‌سازی شده

| نام نمودار | کاربرد | توضیح |
|------------|--------|-------|
| **Histogram** | نمایش توزیع فراوانی | داده‌ها رو به دسته‌ها تقسیم می‌کنه و تعداد هر دسته رو نشون میده |
| **KDE (Kernel Density Estimation)** | تخمین چگالی | نسخه صاف‌شده هیستوگرام - چگالی احتمال رو نشون میده |
| **ECDF (Empirical CDF)** | توزیع تجمعی | درصد داده‌هایی که کمتر از یک مقدار خاص هستند رو نمایش میده |
| **Box Plot** | چارک‌ها و اوتلایرها | میانه، چارک‌ها و اوتلایرها رو به صورت بصری نمایش میده |

## 🧹 روش‌های تمیز کردن داده

### IQR (Interquartile Range)
```python
Q1 = data.quantile(0.25)
Q3 = data.quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR
