import pre_etl
import etl_dim_users
import etl_fact_tickets
import etl_fact_tickets_count

pre_etl.main()
etl_dim_users.copy_users()
etl_fact_tickets.copy_tickets()
etl_fact_tickets_count.insert_data()
