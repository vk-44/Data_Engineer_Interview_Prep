from pyspark.sql.functions import avg, year

salary_avg = (
    salary
    .withColumn("year", year("date"))
    .groupBy("emp_id", "year")
    .agg(avg("salary").alias("avg_sal"))
)

final_df = (
    employee
    .join(salary_avg, on="emp_id", how="inner")
    .select("employee_name", "year", "avg_sal")
)

final_df.show()
