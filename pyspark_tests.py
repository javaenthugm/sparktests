from pyspark.sql import SparkSession

# Create a SparkSession
spark = SparkSession.builder \
    .appName("Read Parquet File") \
    .config("spark.some.config.option", "some-value") \
    .getOrCreate()

# Path to the Parquet file (replace with your file path)
parquet_file_path = "./userdata.parquet"

# Read the Parquet file into a DataFrame
df = spark.read.parquet(parquet_file_path)

# Create a temporary view of the DataFrame
df.createOrReplaceTempView("userdata")

# Show the first 10 rows
print("Displaying the first 10 rows of the DataFrame:")
df.show(10)

# Print schema of the DataFrame
print("Schema of the DataFrame:")
df.printSchema()

# Perform a basic operation (e.g., count rows)
row_count = df.count()
print(f"The DataFrame contains {row_count} rows.")

# Run an SQL query
sql_query = "SELECT email, gender FROM userdata"
result_df = spark.sql(sql_query)

# Show the result of the SQL query
print("Result of the SQL query:")
result_df.show();


# Stop the Spark session
spark.stop()