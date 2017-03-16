# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import unittest, time, re

driver = webdriver.Chrome()
driver.implicitly_wait(30)
base_url = "https://www.redbubble.com/"

# Login
driver.get(base_url + "/auth/login")
driver.find_element_by_id("login-username").clear()
driver.find_element_by_id("login-username").send_keys("bavuongco10")
driver.find_element_by_id("login-password").clear()
driver.find_element_by_id("login-password").send_keys("btbv1994")
driver.find_element_by_id("login-submit").click()

driver.get(base_url + "portfolio/images/new")

# Upload images
driver.find_element_by_id("select-image-single").clear()
driver.find_element_by_id("select-image-single").send_keys("e://1.png")

# choose detail
driver.find_element_by_css_selector("i.rb-font-icon.icon-cancel-circled2").click()
driver.find_element_by_css_selector("div.rb-button.edit-product").click()
driver.find_element_by_css_selector("label.work-config-color-option.body_color_black").click()
driver.find_element_by_css_selector("label.work-config-color-option.body_color_baby_blue").click()
driver.find_element_by_css_selector("span.label-wrap").click()
driver.find_element_by_css_selector("label.back > span.outer-label-wrap > span.label-wrap").click()
driver.find_element_by_css_selector("label.work-config-color-option.body_color_gold").click()
driver.find_element_by_xpath("//button[@value='Center Horizontally']").click()
driver.find_element_by_css_selector("div.buttons > button[name=\"button\"]").click()

#Info
driver.find_element_by_id("work_title").clear()
driver.find_element_by_id("work_title").send_keys("title")
driver.find_element_by_id("work_description_en").clear()
driver.find_element_by_id("work_description_en").send_keys("description")
driver.find_element_by_id("work_tag_field_en").clear()
driver.find_element_by_id("work_tag_field_en").send_keys("tags")
driver.find_element_by_id("media_photography").click()
driver.find_element_by_id("media_digital").click()
driver.find_element_by_id("work_safe_for_work_true").click()

driver.find_element_by_id("submit-work").click()

driver.quit()
