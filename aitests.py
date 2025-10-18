from pyspark.ml.feature import VectorAssembler
from pyspark.ml.classification import LogisticRegression
from pyspark.sql import SparkSession

# Create a SparkSession
spark = SparkSession.builder.appName("AI Tests").getOrCreate()

# Load your data
df = spark.read.parquet("./userdata.parquet")

# Example: Train a logistic regression model to predict 'is_active' (assumed binary column)
# Select features and label columns (replace with actual column names from your data)
feature_columns = ["age", "income"]  # Example feature columns
label_column = "is_active"           # Example label column

# Prepare the data for ML
assembler = VectorAssembler(inputCols=feature_columns, outputCol="features")
ml_df = assembler.transform(df).select("features", label_column)

# Split data into training and test sets
train_df, test_df = ml_df.randomSplit([0.7, 0.3], seed=42)

# Initialize and train the logistic regression model
lr = LogisticRegression(featuresCol="features", labelCol=label_column)
lr_model = lr.fit(train_df)

# Make predictions on the test set
predictions = lr_model.transform(test_df)

# Show some prediction results
print("Sample predictions:")
predictions.select("features", label_column, "prediction", "probability").show(10)