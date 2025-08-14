#Problem1 - Create pivot tables
import pandas as pd

data = {
    'Student': ['Amit', 'Amit', 'Amit', 'Priya', 'Priya'],
    'Subject': ['Maths', 'Science', 'English', 'Maths', 'Science'],
    'Score': [85, 90, 78, 88, 76]
}

df = pd.DataFrame(data)
print(data)
print(df)

pivotTable = pd.pivot_table(df, index='Student', columns='Subject', values='Score')
print("\nPivot Table - Scores by Student & Subject:")
print(pivotTable)


#Problem2 - Write a Pandas program to Combine two Data Frame objects by filling null values in one Data Frame with non-null values from another Data Frame.  
import pandas as pd
import numpy as np

df1 = pd.DataFrame({
    'A': [np.nan, 0.0, np.nan],
    'B': [3, 4, 5]
})

df2 = pd.DataFrame({
    'A': [1, 1, 3],
    'B': [3.0, np.nan, 3.0]
})

print(df1)

print(df2)

result = df1.combine_first(df2)

print("\nCombined DataFrame:")
print(result)


#Problem3 - Write a NumPy program to create a 5x5 array with random values and calculate the exponential of each element.
import numpy as np

arr = np.random.randint(1, 6, size=(5, 5))
print(arr)

expArr = np.exp(arr)
print(expArr)


#Problem4 - Assume you have three Data Frames: sales_df, customers_df, and products_df. The sales_df contains information about sales 
#transactions, including columns such as customer_id, product_id, and quantity_sold. The customers_df contains information about 
# customers, including columns customer_id, customer_name, and customer_location. The products_df contains information about products, 
# including columns product_id, product_name, and category. 

import pandas as pd

sales_df = pd.DataFrame({
    'customer_id': [1, 2, 1, 3],
    'product_id': [101, 102, 103, 101],
    'quantity_sold': [2, 1, 5, 3]
})

customers_df = pd.DataFrame({
    'customer_id': [1, 2, 3],
    'customer_name': ['Amit', 'Priya', 'Rohan'],
    'customer_location': ['Delhi', 'Mumbai', 'Bangalore']
})

products_df = pd.DataFrame({
    'product_id': [101, 102, 103],
    'product_name': ['Laptop', 'Phone', 'Tablet'],
    'category': ['Electronics', 'Electronics', 'Electronics'],
    'price_per_unit': [50000, 20000, 30000] 
})

print(sales_df)
print(customers_df)
print(products_df)

#1 Merge the sales_df with the customers_df on the customer_id column to create a new Data Frame merged_sales_customers_df that 
# includes information about each sale along with the customer details. 

merged_sales_customers_df = pd.merge(sales_df, customers_df, on = 'customer_id',how = 'inner')
print("Merged Sales + Customers DataFrame:")
print(merged_sales_customers_df)


#2 Concatenate the products_df with merged_sales_customers_df along the column's axis, creating a new Data Frame final_df that 
# combines information about sales, customers, and products for each transaction. 

products_df_for_concat = products_df.drop(columns=['product_id'])
final_df = pd.concat([merged_sales_customers_df, products_df_for_concat], axis=1)
print("\nFinal DataFrame after concatenation:")
print(final_df)


#3 Join the final_df with the products_df again, this time on the product_id column, to create a Data Frame complete_sales_df that 
# includes details about each sale, the associated customer, and the corresponding product information. 

complete_sales_df = pd.merge(final_df, products_df, on = 'product_id', how = 'left', suffixes=('_left', '_right'))
print("\nComplete Sales DataFrame after join:")
print(complete_sales_df)


#4: Calculate the total quantity sold and revenue for each product category in the complete_sales_df Data Frame. 

complete_sales_df['revenue'] = complete_sales_df['quantity_sold'] * complete_sales_df['price_per_unit_right']
category_summary = complete_sales_df.groupby('category_right').agg(
    total_quantity_sold=('quantity_sold', 'sum'),
    total_revenue=('revenue', 'sum')
).reset_index()

print("\nCategory-wise Sales Summary:")
print(category_summary)