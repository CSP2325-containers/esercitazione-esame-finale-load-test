from locust import HttpUser, TaskSet, task, between
from bs4 import BeautifulSoup


class CCLUser(HttpUser):
    wait_time = between(1, 5)  # Simula un tempo di attesa tra 1 e 5 secondi
    host = "https://backoffice.cassacommercioliguria.it"
    
    @task
    def view_application_crud(self):
        self.client.get("/?crudAction=index&crudControllerFqcn=App%5CController%5CAdmin%5CApplicationCrudController")
    
    @task
    def view_application_group_420(self):
        self.client.get("/?crudAction=edit&crudControllerFqcn=App%5CController%5CAdmin%5CApplicationGroupCrudController&entityId=420")
    
    @task
    def view_application_detail(self):
        self.client.get("/?crudAction=detail&crudControllerFqcn=App%5CController%5CAdmin%5CApplicationCrudController&entityId=1206&page=1&sort%5Bid%5D=DESC")
        
    @task
    def view_application_detail_2(self):
        self.client.get("/?crudAction=detail&crudControllerFqcn=App%5CController%5CAdmin%5CApplicationCrudController&entityId=1202&page=1&sort%5Bid%5D=DESC")    
    
    @task
    def view_application_group(self):
        self.client.get("/?crudAction=index&crudControllerFqcn=App%5CController%5CAdmin%5CApplicationGroupCrudController") 
    
    @task(3)
    def eb_health_check(self):
        self.client.get("/elbHealthCheck")
        