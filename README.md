# Tata Data Visualization and Cleaning Project  

## 📊 Project Overview  
This project is part of the **Tata Data Visualisation: Empowering Business with Effective Insights** virtual experience program on **Forage**.  
I performed data cleaning using **Python (Pandas)** and created business dashboards using **Power BI** to analyze the **Online Retail Dataset**.  

The project aims to deliver actionable insights for business decision-makers by leveraging clean data and meaningful visualizations.  

---

## 🛠️ Tools & Technologies Used  
- Python (Pandas, NumPy) for Data Cleaning  
- Power BI for Data Visualization  

---



## 📂 Repository Contents  
| File / Folder                  | Description                          |
|--------------------------------|--------------------------------------|
| `data clean.py`                | Python script for data cleaning     |
| `Online_Retail_Cleaned.zip`    | Cleaned dataset in ZIP format        |
| `Online Retail Data Set.zip`   | Original dataset in ZIP format       |
| `Empowering_Insights_Tata_Course_Project.pbix` | Power BI Report file |
| `Dashboard_Overview.jpg`       | Dashboard overview screenshot        |
| `Global_Sales_Overview_Excluding_UK.jpg` | Power BI visual screenshot |
| `Product_Performance_Overview.jpg` | Product performance dashboard |
| `page_information.jpg`         | Dashboard page information overview  |
| `popup_filters.png`            | Power BI filters popup view          |
| `README.md`                    | Project documentation                |

---

## 🧹 Data Cleaning Summary  

Before Cleaning:  
```
Initial Null Values:
InvoiceNo           0
StockCode           0
Description      1454
Quantity            0
InvoiceDate         0
UnitPrice           0
CustomerID     135080
Country             0

Number of Duplicate Rows: 5268
Total Rows Before Cleaning: 541909

Invalid Rows (Quantity < 1): 10624
Invalid Rows (UnitPrice < 0): 2
```

---

After Cleaning:  
```
Missing Values After Cleaning:
InvoiceNo      0
StockCode      0
Description    0
Quantity       0
InvoiceDate    0
UnitPrice      0
CustomerID     0
Country        0

Total Rows After Cleaning: 392732

Invalid Rows (Quantity < 1) After Cleaning: 0
Invalid Rows (UnitPrice < 0) After Cleaning: 0
```

---

✅ The data cleaning process ensured that all missing values, invalid entries, and duplicates were handled before moving to the visualization phase.


---

## 📸 Power BI Dashboard Snapshots  

### 📝 Page 1 — Global Sales Overview (Including UK)  


![Dashboard Overview jpg](https://github.com/user-attachments/assets/3ad4199f-e8b5-48a4-a430-087e01c34b49)


---


###  — Filter Section Overview  
<img width="1289" height="718" alt="popup filters jpg" src="https://github.com/user-attachments/assets/53f11c13-d0a2-41a4-a93c-865712d4e90b" />


---

### 🌍 Page 2 — Global Sales Overview (Excluding UK)  

![Global Sales Overview (Excluding UK) jpg](https://github.com/user-attachments/assets/9acdaeae-5d61-4b4e-8f46-8508c7921cca)

---

### 📦 Page 3 — Product Performance Overview  

![Product Performance Overview jpg](https://github.com/user-attachments/assets/2c5077b9-5564-4025-8e76-2eb054cbd438)


---

### ℹ️ Page 4 — Page Information   
 
![page information jpg](https://github.com/user-attachments/assets/f42e3fed-8add-4f7c-aef7-ad80fef2f3be)

---

These dashboards present key insights like revenue trends, top-performing countries, customer performance, and global sales distribution.






## 📥 How to Use This Project  
- 🔹 Clone or download the repository  
- 🔹 Extract datasets from ZIP files  
- 🔹 Open `data clean.py` for Python data cleaning steps  
- 🔹 Open `.pbix` file in Power BI Desktop to explore dashboards  

---

## 🎯 Key Insights Delivered  
- Revenue trends and top-performing months  
- Top 10 countries and customers by sales  
- Market insights excluding the UK region  
- Product-level sales performance  

---

## 📢 Acknowledgment  
This project was completed as part of the **Tata Data Visualisation Virtual Experience Program** offered by **Forage**.  

---

## ⭐ Feel free to ⭐ star this repo if you found it useful!
