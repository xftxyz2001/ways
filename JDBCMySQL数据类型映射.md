## 类型映射
java.sql.Types定义了常用数据库(MySQL、Oracle、DB2等)所用到的数据类型，官名也叫JDBC类型。每个数据库产品的数据类型定义各不相同，但都有JDBC类型与之对应，如MySQL的BIGINT-->JDBC的BIGINT。

而每个JDBC类型，都有默认的Java类型与之对应，即ResultSet.getObject()返回Object的具体类型，如JDBC的BIGINT-->Java的java.lang.Long；JDBC的BIGINT UNSIGNED-->Java的 java.math.BigInteger。

我们可以通过ResultSet.getMetaData().getColumnTypeName(columnIndex)获取字段的JDBC类型，通过ResultSet.getMetaData().getColumnClassName(columnIndex)获取字段的Java类型。

下表展示了MySQL类型类型、JDBC类型、Java类型的映射关系（源自：5.3 Java, JDBC and MySQL Types）。

| MySQL数据类型                | JDBC类型(getColumnTypeName) | 默认返回的Java类型(getColumnClassName)                                                                                                             |
| ---------------------------- | --------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| BIT(1) (new in MySQL-5.0)    | BIT                         | java.lang.Boolean                                                                                                                                  |
| BIT( > 1) (new in MySQL-5.0) | BIT                         | byte[]                                                                                                                                             |
| TINYINT                      | TINYINT                     | java.lang.Boolean if the configuration property tinyInt1isBit is set to true (the default) and the storage size is 1, or java.lang.Integer if not. |
| BOOL, BOOLEAN                | TINYINT                     | See TINYINT, above as these are aliases for TINYINT(1), currently.                                                                                 |
| SMALLINT[(M)] [UNSIGNED]     | SMALLINT [UNSIGNED]         | java.lang.Integer (regardless of whether it is UNSIGNED or not)                                                                                    |
| MEDIUMINT[(M)] [UNSIGNED]    | MEDIUMINT [UNSIGNED]        | java.lang.Integer (regardless of whether it is UNSIGNED or not)                                                                                    |
| INT,INTEGER[(M)] [UNSIGNED]  | INTEGER [UNSIGNED]          | java.lang.Integer, if UNSIGNED java.lang.Long                                                                                                      |
| BIGINT[(M)] [UNSIGNED]       | BIGINT [UNSIGNED]           | java.lang.Long, if UNSIGNED java.math.BigInteger                                                                                                   |
| FLOAT[(M,D)]                 | FLOAT                       | java.lang.Float                                                                                                                                    |
| DOUBLE[(M,B)]                | DOUBLE                      | java.lang.Double                                                                                                                                   |
| DECIMAL[(M[,D])]             | DECIMAL                     | java.math.BigDecimal                                                                                                                               |
| DATE                         | DATE                        | java.sql.Date                                                                                                                                      |
| DATETIME                     | DATETIME                    | java.sql.Timestamp                                                                                                                                 |
| TIMESTAMP[(M)]               | TIMESTAMP                   | java.sql.Timestamp                                                                                                                                 |
| TIME                         | TIME                        | java.sql.Time                                                                                                                                      |
| YEAR[(2                      | 4)]                         | YEAR                                                                                                                                               | If yearIsDateType configuration property is set to false, then the returned object type is java.sql.Short. If set to true (the default), then the returned object is of type java.sql.Datewith the date set to January 1st, at midnight. |
| CHAR(M)                      | CHAR                        | java.lang.String (unless the character set for the column is BINARY, then byte[] is returned.                                                      |
| VARCHAR(M) [BINARY]          | VARCHAR                     | java.lang.String (unless the character set for the column is BINARY, then byte[] is returned.                                                      |
| BINARY(M)                    | BINARY                      | byte[]                                                                                                                                             |
| VARBINARY(M)                 | VARBINARY                   | byte[]                                                                                                                                             |
| TINYBLOB                     | TINYBLOB                    | byte[]                                                                                                                                             |
| TINYTEXT                     | VARCHAR                     | java.lang.String                                                                                                                                   |
| BLOB                         | BLOB                        | byte[]                                                                                                                                             |
| TEXT                         | VARCHAR                     | java.lang.String                                                                                                                                   |
| MEDIUMBLOB                   | MEDIUMBLOB                  | byte[]                                                                                                                                             |
| MEDIUMTEXT                   | VARCHAR                     | java.lang.String                                                                                                                                   |
| LONGBLOB                     | LONGBLOB                    | byte[]                                                                                                                                             |
| LONGTEXT                     | VARCHAR                     | java.lang.String                                                                                                                                   |
| ENUM('value1','value2',...)  | CHAR                        | java.lang.String                                                                                                                                   |
| SET('value1','value2',...)   | CHAR                        | java.lang.String                                                                                                                                   |


## 类型转换
上面我们看到MySQL的BIGINT默认转为Java的java.lang.Long，那是不是就不能转为String或其他数值类型了？答案是否定的！MySQL的JDBC(Connector/J)在字段类型与Java类型之间的转换是比较灵活的。一般来说，任何字段类型都可以转换为java.lang.String，任何数值字段类型都可以转换为Java的数据类型（当然会出现四舍五入、溢出、精度丢失的问题）。

下图展示了MySQL JDBC允许的跨类型相互转换。 

| MySQL数据类型                                                                                  | 可以被转换的Java类型                                                                                         |
| ---------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------ |
| CHAR, VARCHAR, BLOB, TEXT, ENUM, and SET                                                       | java.lang.String, java.io.InputStream, java.io.Reader, java.sql.Blob, java.sql.Clob                          |
| FLOAT, REAL, DOUBLE PRECISION, NUMERIC, DECIMAL, TINYINT, SMALLINT, MEDIUMINT, INTEGER, BIGINT | java.lang.String, java.lang.Short, java.lang.Integer, java.lang.Long, java.lang.Double, java.math.BigDecimal |
| DATE, TIME, DATETIME, TIMESTAMP                                                                | java.lang.String, java.sql.Date, java.sql.Timestamp                                                          |


## MyBatis
MySQL JDBC对每种字段类型，都有相应的Java类型与之对应，也可以转换为其他Java类型。但这种转换还不够灵活，如TIMESTAMP与java.util.Date就转换不了，只能人工转换。这里推荐使用MyBatis，它内置了许多TypeHander，支持各种基础数据类型间的转换（xxxTypeHandler），也支持自定义数据类型转换。
