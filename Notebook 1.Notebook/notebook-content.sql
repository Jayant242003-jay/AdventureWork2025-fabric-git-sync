-- Fabric notebook source

-- METADATA ********************

-- META {
-- META   "kernel_info": {
-- META     "name": "synapse_pyspark"
-- META   },
-- META   "dependencies": {
-- META     "lakehouse": {
-- META       "default_lakehouse": "bdad926d-f179-48f9-84f7-86fb7d351751",
-- META       "default_lakehouse_name": "Admin_control",
-- META       "default_lakehouse_workspace_id": "e45e058c-5aaa-4a3e-a690-b7759705bf4b",
-- META       "known_lakehouses": [
-- META         {
-- META           "id": "bdad926d-f179-48f9-84f7-86fb7d351751"
-- META         }
-- META       ]
-- META     }
-- META   }
-- META }

-- CELL ********************

CREATE TABLE ControlTable (
    ControlID INT NOT NULL,
    CustomerName VARCHAR(100),
    WorkspaceName VARCHAR(100),
    LakehouseName VARCHAR(100),
    Status VARCHAR(20)
);

-- METADATA ********************

-- META {
-- META   "language": "sparksql",
-- META   "language_group": "synapse_pyspark"
-- META }

-- CELL ********************

INSERT INTO ControlTable (ControlID, CustomerName, WorkspaceName, LakehouseName, Status)
VALUES 
(1, 'Reliance Industries', 'WS_Retail_Prod', 'LH_Reliance_Sales', 'Active'),
(2, 'Tata Consultancy', 'WS_Finance_Dev', 'LH_Tata_Audit', 'Inactive'),
(3, 'HDFC Bank', 'WS_Banking_UAT', 'LH_HDFC_Transactions', 'Pending'),
(4, 'Infosys Tech', 'WS_HR_Global', 'LH_Infy_Employees', 'Active'),
(5, 'Airtel Digital', 'WS_Telecom_Test', 'LH_Airtel_Network', 'Completed');

-- METADATA ********************

-- META {
-- META   "language": "sparksql",
-- META   "language_group": "synapse_pyspark"
-- META }

-- CELL ********************

SELECT * FROM Admin_control.dbo.controltable LIMIT 1000

-- METADATA ********************

-- META {
-- META   "language": "sparksql",
-- META   "language_group": "synapse_pyspark"
-- META }
