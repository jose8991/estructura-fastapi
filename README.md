# fastapi-tools


##variables de entorno

###base de datos
mysql =  mysql+mysqldb://{user}:{password}@{ip}:{port}/{dba}
DATABASE_URL_SQLITE = sqlite:///ecommerce.db
####conexion con la base de datos con postgresql
DATABASE_URL_POSTGRESQL = postgresql://{user}:{password}@{host}:{puerto}/{database}
####conexion con la base de datos con oracle
DATABASE_URL_ORACLE = oracle+cx_oracle://{user}:{password}@{host}:{puerto}/{database}
####conexion con la base de datos con mssql
DATABASE_URL_MSSQL = mssql+pyodbc://{user}:{password}@{host}:{puerto}/{database}
