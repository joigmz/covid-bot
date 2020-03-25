#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 01:10:07 2020

@author: jose izam montt
         Javiera Bustos
"""

from selenium import webdriver
import pandas as pd
import time

def mensaje_covid(pais):
    html = 'https://www.worldometers.info/coronavirus/#countries'
    df = pd.read_html(html)[0]
    
    df = df[df['Country,Other']==pais]
    total_cases = str(df['TotalCases'].item())
    new_cases = str(df['NewCases'].item())
    total_deaths = str(df['TotalDeaths'].item())
    new_deaths = str(df['NewDeaths'].item())
    active_cases = str(df['ActiveCases'].item())
    total_recovered = str(df['TotalRecovered'].item())
    serious_critical = str(df['Serious,Critical'].item())
    
    mensaje = ['Hoy en '+pais,
               'Total casos: ',
               'Nuevos casos: ',
               'Total fallecidos: ',
               'Nuevos fallecidos: ',
               'Casos activos: ',
               'Total recuperados: ',
               'Casos críticos: ']
    
    variables =[ total_cases,
                new_cases,
                total_deaths, 
                new_deaths, 
                active_cases,
                total_recovered, 
                serious_critical]
    
    mensage='Hoy en '+pais

    
    for i in range(len(variables)):
        mensage+= ('\n'+ mensaje[i+1] + str(variables[i]))
        
    return mensage




def busca_frase(ultimo_mensaje,alerta):
    for i in range(len(ultimo_mensaje)):
            completa=''
    
            if ultimo_mensaje[i] == 'c':
                for j in range(len(alerta)):
                    
                    if ultimo_mensaje[i+j]==alerta[j]:
                        completa += ultimo_mensaje[i+j]
    
                        if completa==alerta:
                            print('encontramos el virus')
                            encontrado=1
                            return encontrado
                        
                        
                        
                        
def web_bot():
    
    web='https://www.instagram.com/'
    driver = webdriver.Chrome("/Users/joseizammontt/Desktop/Privado/botlike/bot/chromedriver")
    web_url= web
    driver.get(web_url)
    time.sleep(4)
    
    driver.find_element_by_name("username").send_keys("covid19_bot")
    time.sleep(2)
    driver.find_element_by_name("password").send_keys("Lagloriosa19")
    time.sleep(2)
    
    driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[4]/button/div').click()
    time.sleep(5)
    
    driver.find_element_by_xpath('//*[@class="aOOlW   HoLwm "]').click()
    time.sleep(3)
 
    driver.get('https://www.instagram.com/direct/inbox/')
    time.sleep(2)
    
    driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[1]/div[2]/div/div/div/div/div[1]').click()
    time.sleep(2)
  


    
    encendido_bot =1
    aux_ultimo_mensaje=''
    
    while (encendido_bot==1):
            posts = driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[1]/div[2]/div/div/div/div/div[1]')
            time.sleep(0.1)
            
            ultimo_mensaje= posts.text
            
            if ultimo_mensaje!= aux_ultimo_mensaje:
                print(ultimo_mensaje)
                valor=0
                valor = busca_frase(ultimo_mensaje,'covid-19')

                if valor == 1:
                    mensaje = mensaje_covid('Chile')
                    driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea').send_keys(mensaje)
                    time.sleep(1)
                    driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button').click()
                    
            aux_ultimo_mensaje= ultimo_mensaje
    
    
    #driver.close()
    

web_bot()


                    
  
      


    
    
    
    