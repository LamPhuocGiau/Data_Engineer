# PySpark
- [Start with PySpart](#Start-with-PySpart)

Resilient Distributed Datasets.

![alt text](https://github.com/LamPhuocGiau/Data_Engineer/blob/submain/Theories/Images/Resilient-distributed-datasets.png)

## Start with PySpart

Start a new session and save it as spark.

```
from pyspark.sql import SparkSession
spark = SparkSession.builder.getOrCreate()
```

**Default setting from data saved locally**.

```
rdd_par = spark.sparkContext.parallelize(dataset_name)

```
sparkContext: connect to the cluster.

parallelize(): create an RDDfrom data saved locally.

**External dataset**.

```
# with partition argument of 10
rdd_txt = spark.sparkContext.textFile("file_name.txt", 10)
```
TextFile(): create an RDD.

**Verify the number of partition**.

```
rdd_txt.getNumPartitions()
# output: 10
```
**End SparkSession**.

```
spark.stop()
```
