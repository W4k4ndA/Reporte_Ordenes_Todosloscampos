<h1>Reporte Ordenes Todos Los Campos</h1>

<h3> Introduction</h3>
<p>This code is developed in Python using the Streamlit framework to create a simple web application for a client who wanted
  to improve the way a report, which they regularly use for their daily operations, was generated. The code employs hexagonal 
  architecture, so it also serves as a reference for its use. </p>

  <p>For security reasons, neither the database nor the access data to it are exposed. This application exists on the company's 
    corporate intranet, so although there is always a risk, external threats are minimized. Therefore, the minimum necessary 
    security precautions were taken.</p>

<h3>Explanation</h3>
<p>
  Basically, what this code does is query the database within a time window defined by the user and with the number of fields that
  the user wants to visualize within a wide range of available fields in the query. By changing the connection data and the query, 
  you can get a result adapted to your needs if you wish.
</p>

<h3>Adaptation</h3>
<p>
  To adapt it, you must modify the DBconfig.pyclass in which the connection to the database is built, which will then be used in the 
  MssqlReportRepository.pyclass.
</p>
<p>
  This class is designed to connect to an MS SQL Server database, so if you need to connect to another database, you must download
  the corresponding connector for Python.
</p>
<p>
  The code uses Python's SQLAlchemy module to manage the connection and use of the database.
</p>

<p>The requirements.txt file contains the required modules to the app. Make sureto create a virtual enviroment to launch the app</p>

