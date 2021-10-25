#title: Automate Testing For BITS
#Author: Tandin Wangchuk
#Discription : BITS Admin | BIT | Individual | solo

import time
import HtmlTestRunner
import unittest
from setup import driver

class TestBITS(unittest.TestCase):

    def test_A_admin_Login(self):
        # username
        userName = driver.find_elements_by_xpath(
            "/html/body/app-root/app-auth-layout/div/div[2]/div/app-auth-page/app-basic-login-page/app-auth-form/form/nz-form-item[1]/nz-form-control/div/span/input")[
            0]
        userName.send_keys('admin')
        time.sleep(1)
        # password
        password = driver.find_elements_by_xpath(
            "/html/body/app-root/app-auth-layout/div/div[2]/div/app-auth-page/app-basic-login-page/app-auth-form/form/nz-form-item[2]/nz-form-control/div/span/app-password-input/nz-input-group/input")[
            0]
        password.send_keys('Drc@1239')
        time.sleep(1)
        # submit
        submit = driver.find_elements_by_xpath(
            "/html/body/app-root/app-auth-layout/div/div[2]/div/app-auth-page/app-basic-login-page/app-auth-form/form/nz-form-item[3]/nz-form-control/div/span/button")[
            0]
        submit.click()
        time.sleep(5)
        # self.assertEqual(driver.current_url, "http://10.11.1.13/bits/1bca6d5c-7e79-4bcd-8558-159e3de95810")

    def test_B_create_New_Document(self):
        # driver.get("http://10.11.1.13/bits/47143f65-4b69-401e-8f60-667a26dfdc94")
        driver.get("https://bits.drc.gov.bt/bits/47143f65-4b69-401e-8f60-667a26dfdc94")
        time.sleep(10)
        driver.execute_script('document.querySelector("hatis-renderer").shadowRoot.children[2].querySelector("form-renderer").shadowRoot.querySelector("div").children[2].children[1].querySelector("wc-container").children[1].children[2].children[0].querySelector("wc-button").shadowRoot.querySelector("button").click()')

    def test_C_create_new_agency(self):
        time.sleep(15)
        # select Agency
        driver.execute_script(
            'document.querySelector("body > app-root > app-main-layout > nz-layout > nz-layout > nz-content > div > app-hatis-page > div > hatis-renderer").shadowRoot.querySelector("div.modal > div > div > hatis-renderer").shadowRoot.querySelector("div:nth-child(3) > form-renderer").shadowRoot.querySelector("div > div.main-content > div.container > wc-container > wc-container > wc-container:nth-child(2) > wc-radio-group").shadowRoot.querySelector("#checkbox-92bad1f8-fc2a-4c93-8886-63f96bfea88c").click()')
        # create
        driver.execute_script(
            'document.querySelector("body > app-root > app-main-layout > nz-layout > nz-layout > nz-content > div > app-hatis-page > div > hatis-renderer").shadowRoot.querySelector("div.modal > div > div > hatis-renderer").shadowRoot.querySelector("div:nth-child(3) > form-renderer").shadowRoot.querySelector("div > div.main-content > div.container > wc-container > wc-container > wc-container:nth-child(7) > wc-container:nth-child(1) > wc-button").shadowRoot.querySelector("button").click()')

    def test_D_agency_registration(self):
        time.sleep(15)
        # agency type
        driver.execute_script(
            'document.querySelector("body > app-root > app-main-layout > nz-layout > nz-layout > nz-content > div > app-hatis-page > div > hatis-renderer").shadowRoot.querySelector("div:nth-child(3) > form-renderer").shadowRoot.querySelector("div > div.main-content > div.container > wc-container > wc-container:nth-child(2) > wc-container:nth-child(1) > wc-container:nth-child(4) > wc-container:nth-child(1) > wc-container:nth-child(2) > wc-container > wc-select").shadowRoot.querySelector("#container > select").value = 1')
        driver.execute_script(
            'document.querySelector("body > app-root > app-main-layout > nz-layout > nz-layout > nz-content > div > app-hatis-page > div > hatis-renderer").shadowRoot.querySelector("div:nth-child(3) > form-renderer").shadowRoot.querySelector("div > div.main-content > div.container > wc-container > wc-container:nth-child(2) > wc-container:nth-child(1) > wc-container:nth-child(4) > wc-container:nth-child(1) > wc-container:nth-child(2) > wc-container > wc-select").shadowRoot.querySelector("#container > select").dispatchEvent(new Event("change"))')
        agencytype = driver.execute_script(
            ' return document.querySelector("body > app-root > app-main-layout > nz-layout > nz-layout > nz-content > div > app-hatis-page > div > hatis-renderer").shadowRoot.querySelector("div:nth-child(3) > form-renderer").shadowRoot.querySelector("div > div.main-content > div.container > wc-container > wc-container:nth-child(2) > wc-container:nth-child(1) > wc-container:nth-child(4) > wc-container:nth-child(1) > wc-container:nth-child(2) > wc-container > wc-select").shadowRoot.querySelector("#container > select").value')
        if agencytype != 3:
            # without license
            driver.execute_script(
                'document.querySelector("body > app-root > app-main-layout > nz-layout > nz-layout > nz-content > div > app-hatis-page > div > hatis-renderer").shadowRoot.querySelector("div:nth-child(3) > form-renderer").shadowRoot.querySelector("div > div.main-content > div.container > wc-container > wc-container:nth-child(2) > wc-container:nth-child(1) > wc-container:nth-child(4) > wc-container:nth-child(2) > wc-container:nth-child(1) > wc-radio-group").shadowRoot.querySelector("#checkbox-2").click()')
            time.sleep(5)
            # ministry or agency
            driver.execute_script(
                'document.querySelector("body > app-root > app-main-layout > nz-layout > nz-layout > nz-content > div > app-hatis-page > div > hatis-renderer").shadowRoot.querySelector("div:nth-child(3) > form-renderer").shadowRoot.querySelector("div > div.main-content > div.container > wc-container > wc-container:nth-child(2) > wc-container:nth-child(3) > wc-container:nth-child(2) > wc-container:nth-child(1) > wc-container:nth-child(1) > wc-container:nth-child(2) > wc-container > wc-select").shadowRoot.querySelector("#container > select").value = 1')
            driver.execute_script(
                'document.querySelector("body > app-root > app-main-layout > nz-layout > nz-layout > nz-content > div > app-hatis-page > div > hatis-renderer").shadowRoot.querySelector("div:nth-child(3) > form-renderer").shadowRoot.querySelector("div > div.main-content > div.container > wc-container > wc-container:nth-child(2) > wc-container:nth-child(3) > wc-container:nth-child(2) > wc-container:nth-child(1) > wc-container:nth-child(1) > wc-container:nth-child(2) > wc-container > wc-select").shadowRoot.querySelector("#container > select").dispatchEvent(new Event("change"))')
            # department
            driver.execute_script(
                'document.querySelector("body > app-root > app-main-layout > nz-layout > nz-layout > nz-content > div > app-hatis-page > div > hatis-renderer").shadowRoot.querySelector("div:nth-child(3) > form-renderer").shadowRoot.querySelector("div > div.main-content > div.container > wc-container > wc-container:nth-child(2) > wc-container:nth-child(3) > wc-container:nth-child(2) > wc-container:nth-child(1) > wc-container:nth-child(2) > wc-container > wc-container:nth-child(2) > wc-select").shadowRoot.querySelector("#container > select").value = 1')
            driver.execute_script(
                'document.querySelector("body > app-root > app-main-layout > nz-layout > nz-layout > nz-content > div > app-hatis-page > div > hatis-renderer").shadowRoot.querySelector("div:nth-child(3) > form-renderer").shadowRoot.querySelector("div > div.main-content > div.container > wc-container > wc-container:nth-child(2) > wc-container:nth-child(3) > wc-container:nth-child(2) > wc-container:nth-child(1) > wc-container:nth-child(2) > wc-container > wc-container:nth-child(2) > wc-select").shadowRoot.querySelector("#container > select").dispatchEvent(new Event("change"))')
            # organization name
            driver.execute_script(
                'document.querySelector("body > app-root > app-main-layout > nz-layout > nz-layout > nz-content > div > app-hatis-page > div > hatis-renderer").shadowRoot.querySelector("div:nth-child(3) > form-renderer").shadowRoot.querySelector("div > div.main-content > div.container > wc-container > wc-container:nth-child(2) > wc-container:nth-child(3) > wc-container:nth-child(2) > wc-container:nth-child(2) > wc-container:nth-child(1) > wc-container > wc-container:nth-child(2) > wc-input").shadowRoot.querySelector("#container > input").value = "Testing Bhutan"')
            driver.execute_script(
                'document.querySelector("body > app-root > app-main-layout > nz-layout > nz-layout > nz-content > div > app-hatis-page > div > hatis-renderer").shadowRoot.querySelector("div:nth-child(3) > form-renderer").shadowRoot.querySelector("div > div.main-content > div.container > wc-container > wc-container:nth-child(2) > wc-container:nth-child(3) > wc-container:nth-child(2) > wc-container:nth-child(2) > wc-container:nth-child(1) > wc-container > wc-container:nth-child(2) > wc-input").shadowRoot.querySelector("#container > input").dispatchEvent(new Event("input"))')
            # region
            driver.execute_script(
                'document.querySelector("body > app-root > app-main-layout > nz-layout > nz-layout > nz-content > div > app-hatis-page > div > hatis-renderer").shadowRoot.querySelector("div:nth-child(3) > form-renderer").shadowRoot.querySelector("div > div.main-content > div.container > wc-container > wc-container:nth-child(2) > wc-container:nth-child(3) > wc-container:nth-child(2) > wc-container:nth-child(2) > wc-container:nth-child(2) > wc-container > wc-container:nth-child(2) > wc-container > wc-select").shadowRoot.querySelector("#container > select").value = "TH"')
            driver.execute_script(
                'document.querySelector("body > app-root > app-main-layout > nz-layout > nz-layout > nz-content > div > app-hatis-page > div > hatis-renderer").shadowRoot.querySelector("div:nth-child(3) > form-renderer").shadowRoot.querySelector("div > div.main-content > div.container > wc-container > wc-container:nth-child(2) > wc-container:nth-child(3) > wc-container:nth-child(2) > wc-container:nth-child(2) > wc-container:nth-child(2) > wc-container > wc-container:nth-child(2) > wc-container > wc-select").shadowRoot.querySelector("#container > select").dispatchEvent(new Event("change"))')
            # agency role
            driver.execute_script(
                'document.querySelector("body > app-root > app-main-layout > nz-layout > nz-layout > nz-content > div > app-hatis-page > div > hatis-renderer").shadowRoot.querySelector("div:nth-child(3) > form-renderer").shadowRoot.querySelector("div > div.main-content > div.container > wc-container > wc-container:nth-child(2) > wc-container:nth-child(3) > wc-container:nth-child(2) > wc-container:nth-child(3) > wc-container > wc-container:nth-child(1) > wc-container:nth-child(2) > wc-container:nth-child(2) > wc-container > wc-multi-select").shadowRoot.querySelector("#itemList > div:nth-child(1) > input[type=checkbox]").click()')
            # mobile number
            driver.execute_script(
                'document.querySelector("body > app-root > app-main-layout > nz-layout > nz-layout > nz-content > div > app-hatis-page > div > hatis-renderer").shadowRoot.querySelector("div:nth-child(3) > form-renderer").shadowRoot.querySelector("div > div.main-content > div.container > wc-container > wc-container:nth-child(2) > wc-container:nth-child(4) > wc-container:nth-child(2) > wc-fractal").shadowRoot.querySelector("slot > wc-slot > wc-container:nth-child(1) > wc-container:nth-child(2) > wc-container > wc-container:nth-child(1) > wc-container:nth-child(2) > wc-container:nth-child(1) > wc-input").shadowRoot.querySelector("#container > input").value = 17231231')
            driver.execute_script(
                'document.querySelector("body > app-root > app-main-layout > nz-layout > nz-layout > nz-content > div > app-hatis-page > div > hatis-renderer").shadowRoot.querySelector("div:nth-child(3) > form-renderer").shadowRoot.querySelector("div > div.main-content > div.container > wc-container > wc-container:nth-child(2) > wc-container:nth-child(4) > wc-container:nth-child(2) > wc-fractal").shadowRoot.querySelector("slot > wc-slot > wc-container:nth-child(1) > wc-container:nth-child(2) > wc-container > wc-container:nth-child(1) > wc-container:nth-child(2) > wc-container:nth-child(1) > wc-input").shadowRoot.querySelector("#container > input").dispatchEvent(new Event("input"))')
            # id document type
            driver.execute_script(
                'document.querySelector("body > app-root > app-main-layout > nz-layout > nz-layout > nz-content > div > app-hatis-page > div > hatis-renderer").shadowRoot.querySelector("div:nth-child(3) > form-renderer").shadowRoot.querySelector("div > div.main-content > div.container > wc-container > wc-container:nth-child(2) > wc-container:nth-child(5) > wc-container:nth-child(2) > wc-container:nth-child(2) > wc-container:nth-child(1) > wc-container:nth-child(1) > wc-container:nth-child(1) > wc-container:nth-child(3) > wc-select").shadowRoot.querySelector("#container > select").value = 7')
            driver.execute_script(
                'document.querySelector("body > app-root > app-main-layout > nz-layout > nz-layout > nz-content > div > app-hatis-page > div > hatis-renderer").shadowRoot.querySelector("div:nth-child(3) > form-renderer").shadowRoot.querySelector("div > div.main-content > div.container > wc-container > wc-container:nth-child(2) > wc-container:nth-child(5) > wc-container:nth-child(2) > wc-container:nth-child(2) > wc-container:nth-child(1) > wc-container:nth-child(1) > wc-container:nth-child(1) > wc-container:nth-child(3) > wc-select").shadowRoot.querySelector("#container > select").dispatchEvent(new Event("change"))')
            # id number
            driver.execute_script(
                'document.querySelector("body > app-root > app-main-layout > nz-layout > nz-layout > nz-content > div > app-hatis-page > div > hatis-renderer").shadowRoot.querySelector("div:nth-child(3) > form-renderer").shadowRoot.querySelector("div > div.main-content > div.container > wc-container > wc-container:nth-child(2) > wc-container:nth-child(5) > wc-container:nth-child(2) > wc-container:nth-child(2) > wc-container:nth-child(1) > wc-container:nth-child(1) > wc-container:nth-child(2) > wc-container:nth-child(3) > wc-container:nth-child(1) > wc-input").shadowRoot.querySelector("#container > input").value = 11905001127')
            driver.execute_script(
                'document.querySelector("body > app-root > app-main-layout > nz-layout > nz-layout > nz-content > div > app-hatis-page > div > hatis-renderer").shadowRoot.querySelector("div:nth-child(3) > form-renderer").shadowRoot.querySelector("div > div.main-content > div.container > wc-container > wc-container:nth-child(2) > wc-container:nth-child(5) > wc-container:nth-child(2) > wc-container:nth-child(2) > wc-container:nth-child(1) > wc-container:nth-child(1) > wc-container:nth-child(2) > wc-container:nth-child(3) > wc-container:nth-child(1) > wc-input").shadowRoot.querySelector("#container > input").dispatchEvent(new Event("input"))')
            # search
            driver.execute_script(
                'document.querySelector("body > app-root > app-main-layout > nz-layout > nz-layout > nz-content > div > app-hatis-page > div > hatis-renderer").shadowRoot.querySelector("div:nth-child(3) > form-renderer").shadowRoot.querySelector("div > div.main-content > div.container > wc-container > wc-container:nth-child(2) > wc-container:nth-child(5) > wc-container:nth-child(2) > wc-container:nth-child(2) > wc-container:nth-child(1) > wc-container:nth-child(1) > wc-container:nth-child(2) > wc-container:nth-child(3) > wc-container:nth-child(1) > wc-container > wc-image").shadowRoot.querySelector("img").click()')
            # mobuile number
            driver.execute_script(
                'document.querySelector("body > app-root > app-main-layout > nz-layout > nz-layout > nz-content > div > app-hatis-page > div > hatis-renderer").shadowRoot.querySelector("div:nth-child(3) > form-renderer").shadowRoot.querySelector("div > div.main-content > div.container > wc-container > wc-container:nth-child(2) > wc-container:nth-child(5) > wc-container:nth-child(2) > wc-container:nth-child(2) > wc-container:nth-child(4) > wc-container > wc-container:nth-child(1) > wc-container:nth-child(2) > wc-input").shadowRoot.querySelector("#container > input").value = 17451312')
            driver.execute_script(
                'document.querySelector("body > app-root > app-main-layout > nz-layout > nz-layout > nz-content > div > app-hatis-page > div > hatis-renderer").shadowRoot.querySelector("div:nth-child(3) > form-renderer").shadowRoot.querySelector("div > div.main-content > div.container > wc-container > wc-container:nth-child(2) > wc-container:nth-child(5) > wc-container:nth-child(2) > wc-container:nth-child(2) > wc-container:nth-child(4) > wc-container > wc-container:nth-child(1) > wc-container:nth-child(2) > wc-input").shadowRoot.querySelector("#container > input").dispatchEvent(new Event("input"))')
            # tel number
            driver.execute_script(
                'document.querySelector("body > app-root > app-main-layout > nz-layout > nz-layout > nz-content > div > app-hatis-page > div > hatis-renderer").shadowRoot.querySelector("div:nth-child(3) > form-renderer").shadowRoot.querySelector("div > div.main-content > div.container > wc-container > wc-container:nth-child(2) > wc-container:nth-child(5) > wc-container:nth-child(2) > wc-container:nth-child(2) > wc-container:nth-child(4) > wc-container > wc-container:nth-child(2) > wc-container:nth-child(2) > wc-input").shadowRoot.querySelector("#container > input").value = 12341238')
            driver.execute_script(
                'document.querySelector("body > app-root > app-main-layout > nz-layout > nz-layout > nz-content > div > app-hatis-page > div > hatis-renderer").shadowRoot.querySelector("div:nth-child(3) > form-renderer").shadowRoot.querySelector("div > div.main-content > div.container > wc-container > wc-container:nth-child(2) > wc-container:nth-child(5) > wc-container:nth-child(2) > wc-container:nth-child(2) > wc-container:nth-child(4) > wc-container > wc-container:nth-child(2) > wc-container:nth-child(2) > wc-input").shadowRoot.querySelector("#container > input").dispatchEvent(new Event("input"))')
            # dzongkhag
            driver.execute_script(
                'document.querySelector("body > app-root > app-main-layout > nz-layout > nz-layout > nz-content > div > app-hatis-page > div > hatis-renderer").shadowRoot.querySelector("div:nth-child(3) > form-renderer").shadowRoot.querySelector("div > div.main-content > div.container > wc-container > wc-container:nth-child(2) > wc-container:nth-child(7) > wc-container:nth-child(2) > wc-container > wc-container:nth-child(4) > wc-container:nth-child(1) > wc-container:nth-child(2) > wc-container > wc-select").shadowRoot.querySelector("#container > select").value = 1')
            driver.execute_script(
                'document.querySelector("body > app-root > app-main-layout > nz-layout > nz-layout > nz-content > div > app-hatis-page > div > hatis-renderer").shadowRoot.querySelector("div:nth-child(3) > form-renderer").shadowRoot.querySelector("div > div.main-content > div.container > wc-container > wc-container:nth-child(2) > wc-container:nth-child(7) > wc-container:nth-child(2) > wc-container > wc-container:nth-child(4) > wc-container:nth-child(1) > wc-container:nth-child(2) > wc-container > wc-select").shadowRoot.querySelector("#container > select").dispatchEvent(new Event("change"))')
            # gewog
            driver.execute_script(
                'document.querySelector("body > app-root > app-main-layout > nz-layout > nz-layout > nz-content > div > app-hatis-page > div > hatis-renderer").shadowRoot.querySelector("div:nth-child(3) > form-renderer").shadowRoot.querySelector("div > div.main-content > div.container > wc-container > wc-container:nth-child(2) > wc-container:nth-child(7) > wc-container:nth-child(2) > wc-container > wc-container:nth-child(5) > wc-container:nth-child(1) > wc-container:nth-child(2) > wc-container > wc-select").shadowRoot.querySelector("#container > select").value = 1')
            driver.execute_script(
                'document.querySelector("body > app-root > app-main-layout > nz-layout > nz-layout > nz-content > div > app-hatis-page > div > hatis-renderer").shadowRoot.querySelector("div:nth-child(3) > form-renderer").shadowRoot.querySelector("div > div.main-content > div.container > wc-container > wc-container:nth-child(2) > wc-container:nth-child(7) > wc-container:nth-child(2) > wc-container > wc-container:nth-child(5) > wc-container:nth-child(1) > wc-container:nth-child(2) > wc-container > wc-select").shadowRoot.querySelector("#container > select").dispatchEvent(new Event("change"))')
            # village
            driver.execute_script(
                'document.querySelector("body > app-root > app-main-layout > nz-layout > nz-layout > nz-content > div > app-hatis-page > div > hatis-renderer").shadowRoot.querySelector("div:nth-child(3) > form-renderer").shadowRoot.querySelector("div > div.main-content > div.container > wc-container > wc-container:nth-child(2) > wc-container:nth-child(7) > wc-container:nth-child(2) > wc-container > wc-container:nth-child(5) > wc-container:nth-child(2) > wc-container:nth-child(2) > wc-container > wc-select").shadowRoot.querySelector("#container > select").value = 1')
            driver.execute_script(
                'document.querySelector("body > app-root > app-main-layout > nz-layout > nz-layout > nz-content > div > app-hatis-page > div > hatis-renderer").shadowRoot.querySelector("div:nth-child(3) > form-renderer").shadowRoot.querySelector("div > div.main-content > div.container > wc-container > wc-container:nth-child(2) > wc-container:nth-child(7) > wc-container:nth-child(2) > wc-container > wc-container:nth-child(5) > wc-container:nth-child(2) > wc-container:nth-child(2) > wc-container > wc-select").shadowRoot.querySelector("#container > select").dispatchEvent(new Event("change"))')
            time.sleep(15)
            # final check
            driver.execute_script(
                'document.querySelector("body > app-root > app-main-layout > nz-layout > nz-layout > nz-content > div > app-hatis-page > div > hatis-renderer").shadowRoot.querySelector("div:nth-child(3) > form-renderer").shadowRoot.querySelector("div > div.main-content > div.container > wc-container > wc-container:nth-child(3) > wc-container:nth-child(3) > wc-container > wc-container:nth-child(1) > wc-checkbox-group").shadowRoot.querySelector("#checkbox-1").click()')

            # submit button
            driver.execute_script(
                'document.querySelector("body > app-root > app-main-layout > nz-layout > nz-layout > nz-content > div > app-hatis-page > div > hatis-renderer").shadowRoot.querySelector("div:nth-child(3) > form-renderer").shadowRoot.querySelector("div > div.main-content > div.container > wc-container > wc-container:nth-child(4) > wc-container:nth-child(3) > wc-container:nth-child(3) > wc-button").shadowRoot.querySelector("button").click()')
        time.sleep(10)
        drnnumber = driver.execute_script(
            'return document.querySelector("body > app-root > app-main-layout > nz-layout > nz-layout > nz-content > div > app-hatis-page > div > hatis-renderer").shadowRoot.querySelector("div.modal > div > div > hatis-renderer").shadowRoot.querySelector("div:nth-child(3) > form-renderer").shadowRoot.querySelector("div > div.main-content > div.container > wc-container > wc-container > wc-container:nth-child(1) > wc-container:nth-child(1) > wc-text").shadowRoot.querySelector("div").innerText.split(".")[1].split(" ")[6]')
        driver.execute_script(
            'document.querySelector("body > app-root > app-main-layout > nz-layout > nz-layout > nz-content > div > app-hatis-page > div > hatis-renderer").shadowRoot.querySelector("div.modal > div > div > hatis-renderer").shadowRoot.querySelector("div:nth-child(3) > form-renderer").shadowRoot.querySelector("div > div.main-content > div.container > wc-container > wc-container > wc-container:nth-child(2) > wc-button").shadowRoot.querySelector("button").click()')
        # navigate to documents
        driver.get('https://bits.drc.gov.bt/bits/47143f65-4b69-401e-8f60-667a26dfdc94')
        time.sleep(10)
        # enter drn
        driver.execute_script(
            'document.querySelector("body > app-root > app-main-layout > nz-layout > nz-layout > nz-content > div > app-hatis-page > div > hatis-renderer").shadowRoot.querySelector("div:nth-child(3) > form-renderer").shadowRoot.querySelector("div > div.main-content > div.container > wc-container > wc-container:nth-child(2) > wc-container:nth-child(2) > wc-container:nth-child(2) > wc-container:nth-child(1) > wc-container:nth-child(2) > wc-input").shadowRoot.querySelector("#container > input").value = ' + '"' + drnnumber + '"' + '')
        driver.execute_script(
            'document.querySelector("body > app-root > app-main-layout > nz-layout > nz-layout > nz-content > div > app-hatis-page > div > hatis-renderer").shadowRoot.querySelector("div:nth-child(3) > form-renderer").shadowRoot.querySelector("div > div.main-content > div.container > wc-container > wc-container:nth-child(2) > wc-container:nth-child(2) > wc-container:nth-child(2) > wc-container:nth-child(1) > wc-container:nth-child(2) > wc-input").shadowRoot.querySelector("#container > input").dispatchEvent(new Event("input"))')
        # search
        driver.execute_script(
            'document.querySelector("body > app-root > app-main-layout > nz-layout > nz-layout > nz-content > div > app-hatis-page > div > hatis-renderer").shadowRoot.querySelector("div:nth-child(3) > form-renderer").shadowRoot.querySelector("div > div.main-content > div.container > wc-container > wc-container:nth-child(2) > wc-container:nth-child(3) > wc-container:nth-child(2) > wc-button").shadowRoot.querySelector("button").click()')
        time.sleep(5)
        # view
        driver.execute_script(
            'document.querySelector("body > app-root > app-main-layout > nz-layout > nz-layout > nz-content > div > app-hatis-page > div > hatis-renderer").shadowRoot.querySelector("div:nth-child(3) > form-renderer").shadowRoot.querySelector("div > div.main-content > div.container > wc-container > wc-container:nth-child(3) > wc-container:nth-child(2) > wc-scroll-container > wc-container:nth-child(4) > wc-fractal").shadowRoot.querySelector("slot > wc-slot > wc-container > wc-container:nth-child(11) > wc-tooltip > wc-image").shadowRoot.querySelector("img").click()')
        time.sleep(10)
        # verify
        driver.execute_script(
            'document.querySelector("body > app-root > app-main-layout > nz-layout > nz-layout > nz-content > div > app-hatis-page > div > hatis-renderer").shadowRoot.querySelector("div:nth-child(3) > form-renderer").shadowRoot.querySelector("div > div.main-content > div.container > wc-container > wc-container:nth-child(4) > wc-container:nth-child(1) > wc-container:nth-child(2) > wc-select").shadowRoot.querySelector("#container > select").value = 3')
        driver.execute_script(
            'document.querySelector("body > app-root > app-main-layout > nz-layout > nz-layout > nz-content > div > app-hatis-page > div > hatis-renderer").shadowRoot.querySelector("div:nth-child(3) > form-renderer").shadowRoot.querySelector("div > div.main-content > div.container > wc-container > wc-container:nth-child(4) > wc-container:nth-child(1) > wc-container:nth-child(2) > wc-select").shadowRoot.querySelector("#container > select").dispatchEvent(new Event("change"))')
        # proceed
        driver.execute_script(
            'document.querySelector("body > app-root > app-main-layout > nz-layout > nz-layout > nz-content > div > app-hatis-page > div > hatis-renderer").shadowRoot.querySelector("div:nth-child(3) > form-renderer").shadowRoot.querySelector("div > div.main-content > div.container > wc-container > wc-container:nth-child(4) > wc-container:nth-child(1) > wc-container:nth-child(3) > wc-button").shadowRoot.querySelector("button").click()')
        time.sleep(5)
        # comment
        driver.execute_script(
            'document.querySelector("body > app-root > app-main-layout > nz-layout > nz-layout > nz-content > div > app-hatis-page > div > hatis-renderer").shadowRoot.querySelector("div.modal > div > div > hatis-renderer").shadowRoot.querySelector("div:nth-child(3) > form-renderer").shadowRoot.querySelector("div > div.main-content > div.container > wc-container > wc-container > wc-container:nth-child(2) > wc-textarea").shadowRoot.querySelector("#container > textarea").value = "verify"')
        driver.execute_script(
            'document.querySelector("body > app-root > app-main-layout > nz-layout > nz-layout > nz-content > div > app-hatis-page > div > hatis-renderer").shadowRoot.querySelector("div.modal > div > div > hatis-renderer").shadowRoot.querySelector("div:nth-child(3) > form-renderer").shadowRoot.querySelector("div > div.main-content > div.container > wc-container > wc-container > wc-container:nth-child(2) > wc-textarea").shadowRoot.querySelector("#container > textarea").dispatchEvent(new Event("input"))')
        # add comment button
        driver.execute_script(
            'document.querySelector("body > app-root > app-main-layout > nz-layout > nz-layout > nz-content > div > app-hatis-page > div > hatis-renderer").shadowRoot.querySelector("div.modal > div > div > hatis-renderer").shadowRoot.querySelector("div:nth-child(3) > form-renderer").shadowRoot.querySelector("div > div.main-content > div.container > wc-container > wc-container > wc-container:nth-child(3) > wc-button").shadowRoot.querySelector("button").click()')
        time.sleep(5)
        # copy drnafter
        drnafter = driver.execute_script(
            'return document.querySelector("body > app-root > app-main-layout > nz-layout > nz-layout > nz-content > div > app-hatis-page > div > hatis-renderer").shadowRoot.querySelector("div.modal > div > div > hatis-renderer").shadowRoot.querySelector("div:nth-child(3) > form-renderer").shadowRoot.querySelector("div > div.main-content > div.container > wc-container > wc-container > wc-container:nth-child(1) > wc-text:nth-child(1)").shadowRoot.querySelector("div").innerText.split(".")[1].split(" ")[6]')
        # ok button
        driver.execute_script(
            'document.querySelector("body > app-root > app-main-layout > nz-layout > nz-layout > nz-content > div > app-hatis-page > div > hatis-renderer").shadowRoot.querySelector("div.modal > div > div > hatis-renderer").shadowRoot.querySelector("div:nth-child(3) > form-renderer").shadowRoot.querySelector("div > div.main-content > div.container > wc-container > wc-container > wc-container:nth-child(2) > wc-button").shadowRoot.querySelector("button").click()')
        # navigate to documents
        driver.get('https://bits.drc.gov.bt/bits/47143f65-4b69-401e-8f60-667a26dfdc94')
        time.sleep(15)
        # enter drn
        driver.execute_script(
            'document.querySelector("body > app-root > app-main-layout > nz-layout > nz-layout > nz-content > div > app-hatis-page > div > hatis-renderer").shadowRoot.querySelector("div:nth-child(3) > form-renderer").shadowRoot.querySelector("div > div.main-content > div.container > wc-container > wc-container:nth-child(2) > wc-container:nth-child(2) > wc-container:nth-child(2) > wc-container:nth-child(1) > wc-container:nth-child(2) > wc-input").shadowRoot.querySelector("#container > input").value = ' + '"' + drnafter + '"' + '')
        driver.execute_script(
            'document.querySelector("body > app-root > app-main-layout > nz-layout > nz-layout > nz-content > div > app-hatis-page > div > hatis-renderer").shadowRoot.querySelector("div:nth-child(3) > form-renderer").shadowRoot.querySelector("div > div.main-content > div.container > wc-container > wc-container:nth-child(2) > wc-container:nth-child(2) > wc-container:nth-child(2) > wc-container:nth-child(1) > wc-container:nth-child(2) > wc-input").shadowRoot.querySelector("#container > input").dispatchEvent(new Event("input"))')
        # search
        driver.execute_script(
            'document.querySelector("body > app-root > app-main-layout > nz-layout > nz-layout > nz-content > div > app-hatis-page > div > hatis-renderer").shadowRoot.querySelector("div:nth-child(3) > form-renderer").shadowRoot.querySelector("div > div.main-content > div.container > wc-container > wc-container:nth-child(2) > wc-container:nth-child(3) > wc-container:nth-child(2) > wc-button").shadowRoot.querySelector("button").click()')
        time.sleep(5)
        # view
        driver.execute_script(
            'document.querySelector("body > app-root > app-main-layout > nz-layout > nz-layout > nz-content > div > app-hatis-page > div > hatis-renderer").shadowRoot.querySelector("div:nth-child(3) > form-renderer").shadowRoot.querySelector("div > div.main-content > div.container > wc-container > wc-container:nth-child(3) > wc-container:nth-child(2) > wc-scroll-container > wc-container:nth-child(4) > wc-fractal").shadowRoot.querySelector("slot > wc-slot > wc-container > wc-container:nth-child(1) > wc-text").shadowRoot.querySelector("div").click()')
        time.sleep(10)
        # approve
        driver.execute_script(
            'document.querySelector("body > app-root > app-main-layout > nz-layout > nz-layout > nz-content > div > app-hatis-page > div > hatis-renderer").shadowRoot.querySelector("div:nth-child(3) > form-renderer").shadowRoot.querySelector("div > div.main-content > div.container > wc-container > wc-container:nth-child(4) > wc-container:nth-child(1) > wc-container:nth-child(2) > wc-select").shadowRoot.querySelector("#container > select").value = 4')
        driver.execute_script(
            'document.querySelector("body > app-root > app-main-layout > nz-layout > nz-layout > nz-content > div > app-hatis-page > div > hatis-renderer").shadowRoot.querySelector("div:nth-child(3) > form-renderer").shadowRoot.querySelector("div > div.main-content > div.container > wc-container > wc-container:nth-child(4) > wc-container:nth-child(1) > wc-container:nth-child(2) > wc-select").shadowRoot.querySelector("#container > select").dispatchEvent(new Event("change"))')
        # proceed
        driver.execute_script(
            'document.querySelector("body > app-root > app-main-layout > nz-layout > nz-layout > nz-content > div > app-hatis-page > div > hatis-renderer").shadowRoot.querySelector("div:nth-child(3) > form-renderer").shadowRoot.querySelector("div > div.main-content > div.container > wc-container > wc-container:nth-child(4) > wc-container:nth-child(1) > wc-container:nth-child(3) > wc-button").shadowRoot.querySelector("button").click()')
        time.sleep(5)
    def test_E_amendment(self):
        # tpn
        tpn = driver.execute_script('return document.querySelector("body > app-root > app-main-layout > nz-layout > nz-layout > nz-content > div > app-hatis-page > div > hatis-renderer").shadowRoot.querySelector("div.modal > div > div > hatis-renderer").shadowRoot.querySelector("div:nth-child(3) > form-renderer").shadowRoot.querySelector("div > div.main-content > div.container > wc-container > wc-container > wc-container:nth-child(1) > wc-container:nth-child(1) > wc-text").shadowRoot.querySelector("div").innerText.split(".")[1].split(" ")[6]')
        #ok button
        driver.execute_script('document.querySelector("body > app-root > app-main-layout > nz-layout > nz-layout > nz-content > div > app-hatis-page > div > hatis-renderer").shadowRoot.querySelector("div.modal > div > div > hatis-renderer").shadowRoot.querySelector("div:nth-child(3) > form-renderer").shadowRoot.querySelector("div > div.main-content > div.container > wc-container > wc-container > wc-container:nth-child(2) > wc-button").shadowRoot.querySelector("button").click()')
        # taxpayer
        driver.get('https://bits.drc.gov.bt/bits/aee128cd-016f-4c8b-8049-f676dbbdd609')
        time.sleep(10)
        # enter tpn
        driver.execute_script('document.querySelector("body > app-root > app-main-layout > nz-layout > nz-layout > nz-content > div > app-hatis-page > div > hatis-renderer").shadowRoot.querySelector("div:nth-child(3) > form-renderer").shadowRoot.querySelector("div > div.main-content > div.container > wc-container > wc-container:nth-child(2) > wc-container:nth-child(1) > wc-container:nth-child(2) > wc-container:nth-child(2) > wc-container:nth-child(1) > wc-container:nth-child(2) > wc-input").shadowRoot.querySelector("#container > input").value = '+'"'+tpn+'"'+'')
        driver.execute_script('document.querySelector("body > app-root > app-main-layout > nz-layout > nz-layout > nz-content > div > app-hatis-page > div > hatis-renderer").shadowRoot.querySelector("div:nth-child(3) > form-renderer").shadowRoot.querySelector("div > div.main-content > div.container > wc-container > wc-container:nth-child(2) > wc-container:nth-child(1) > wc-container:nth-child(2) > wc-container:nth-child(2) > wc-container:nth-child(1) > wc-container:nth-child(2) > wc-input").shadowRoot.querySelector("#container > input").dispatchEvent(new Event("input"))')
        # search
        driver.execute_script('document.querySelector("body > app-root > app-main-layout > nz-layout > nz-layout > nz-content > div > app-hatis-page > div > hatis-renderer").shadowRoot.querySelector("div:nth-child(3) > form-renderer").shadowRoot.querySelector("div > div.main-content > div.container > wc-container > wc-container:nth-child(2) > wc-container:nth-child(1) > wc-container:nth-child(3) > wc-container:nth-child(1) > wc-button").shadowRoot.querySelector("button").click()')
        time.sleep(5)
        # view
        driver.execute_script('document.querySelector("body > app-root > app-main-layout > nz-layout > nz-layout > nz-content > div > app-hatis-page > div > hatis-renderer").shadowRoot.querySelector("div:nth-child(3) > form-renderer").shadowRoot.querySelector("div > div.main-content > div.container > wc-container > wc-container:nth-child(2) > wc-container:nth-child(2) > wc-container:nth-child(2) > wc-scroll-container > wc-fractal").shadowRoot.querySelector("slot > wc-slot > wc-container > wc-container:nth-child(1) > wc-container > wc-text").shadowRoot.querySelector("div").click()')
        time.sleep(15)
        # click on edit
        driver.execute_script('document.querySelector("body > app-root > app-main-layout > nz-layout > nz-layout > nz-content > div > app-hatis-page > div > hatis-renderer").shadowRoot.querySelector("div:nth-child(3) > form-renderer").shadowRoot.querySelector("div > div.main-content > div.container > wc-container > wc-container:nth-child(2) > wc-container:nth-child(1) > wc-container:nth-child(4) > wc-container:nth-child(2) > wc-container:nth-child(2) > wc-container > wc-button").shadowRoot.querySelector("button").click()')
        time.sleep(10)
        # change number
        driver.execute_script('document.querySelector("body > app-root > app-main-layout > nz-layout > nz-layout > nz-content > div > app-hatis-page > div > hatis-renderer").shadowRoot.querySelector("div:nth-child(3) > form-renderer").shadowRoot.querySelector("div > div.main-content > div.container > wc-container > wc-container:nth-child(2) > wc-container:nth-child(4) > wc-container:nth-child(2) > wc-fractal").shadowRoot.querySelector("slot > wc-slot > wc-container:nth-child(1) > wc-container:nth-child(2) > wc-container > wc-container:nth-child(1) > wc-container:nth-child(2) > wc-container:nth-child(1) > wc-input").shadowRoot.querySelector("#container > input").value = "17407438"')
        driver.execute_script('document.querySelector("body > app-root > app-main-layout > nz-layout > nz-layout > nz-content > div > app-hatis-page > div > hatis-renderer").shadowRoot.querySelector("div:nth-child(3) > form-renderer").shadowRoot.querySelector("div > div.main-content > div.container > wc-container > wc-container:nth-child(2) > wc-container:nth-child(4) > wc-container:nth-child(2) > wc-fractal").shadowRoot.querySelector("slot > wc-slot > wc-container:nth-child(1) > wc-container:nth-child(2) > wc-container > wc-container:nth-child(1) > wc-container:nth-child(2) > wc-container:nth-child(1) > wc-input").shadowRoot.querySelector("#container > input").dispatchEvent(new Event("input"))')
        # submit
        driver.execute_script('document.querySelector("body > app-root > app-main-layout > nz-layout > nz-layout > nz-content > div > app-hatis-page > div > hatis-renderer").shadowRoot.querySelector("div:nth-child(3) > form-renderer").shadowRoot.querySelector("div > div.main-content > div.container > wc-container > wc-container:nth-child(4) > wc-container:nth-child(3) > wc-container:nth-child(3) > wc-button").shadowRoot.querySelector("button").click()')
        time.sleep(10)
        # drn
        drnafteredit = driver.execute_script('return document.querySelector("body > app-root > app-main-layout > nz-layout > nz-layout > nz-content > div > app-hatis-page > div > hatis-renderer").shadowRoot.querySelector("div.modal > div > div > hatis-renderer").shadowRoot.querySelector("div:nth-child(3) > form-renderer").shadowRoot.querySelector("div > div.main-content > div.container > wc-container > wc-container > wc-container:nth-child(1) > wc-text:nth-child(1)").shadowRoot.querySelector("div").innerText.split(".")[1].split(" ")[6]')
        # ok button
        driver.execute_script('document.querySelector("body > app-root > app-main-layout > nz-layout > nz-layout > nz-content > div > app-hatis-page > div > hatis-renderer").shadowRoot.querySelector("div.modal > div > div > hatis-renderer").shadowRoot.querySelector("div:nth-child(3) > form-renderer").shadowRoot.querySelector("div > div.main-content > div.container > wc-container > wc-container > wc-container:nth-child(2) > wc-button").shadowRoot.querySelector("button").click()')
        # navigate to document
        driver.get('https://bits.drc.gov.bt/bits/47143f65-4b69-401e-8f60-667a26dfdc94')
        time.sleep(15)
        # enter drn
        driver.execute_script('document.querySelector("body > app-root > app-main-layout > nz-layout > nz-layout > nz-content > div > app-hatis-page > div > hatis-renderer").shadowRoot.querySelector("div:nth-child(3) > form-renderer").shadowRoot.querySelector("div > div.main-content > div.container > wc-container > wc-container:nth-child(2) > wc-container:nth-child(2) > wc-container:nth-child(2) > wc-container:nth-child(1) > wc-container:nth-child(2) > wc-input").shadowRoot.querySelector("#container > input").value = '+'"'+drnafteredit+'"'+'')
        driver.execute_script('document.querySelector("body > app-root > app-main-layout > nz-layout > nz-layout > nz-content > div > app-hatis-page > div > hatis-renderer").shadowRoot.querySelector("div:nth-child(3) > form-renderer").shadowRoot.querySelector("div > div.main-content > div.container > wc-container > wc-container:nth-child(2) > wc-container:nth-child(2) > wc-container:nth-child(2) > wc-container:nth-child(1) > wc-container:nth-child(2) > wc-input").shadowRoot.querySelector("#container > input").dispatchEvent(new Event("input"))')
        # search
        driver.execute_script('document.querySelector("body > app-root > app-main-layout > nz-layout > nz-layout > nz-content > div > app-hatis-page > div > hatis-renderer").shadowRoot.querySelector("div:nth-child(3) > form-renderer").shadowRoot.querySelector("div > div.main-content > div.container > wc-container > wc-container:nth-child(2) > wc-container:nth-child(3) > wc-container:nth-child(2) > wc-button").shadowRoot.querySelector("button").click()')
        time.sleep(5)
        # view
        driver.execute_script('document.querySelector("body > app-root > app-main-layout > nz-layout > nz-layout > nz-content > div > app-hatis-page > div > hatis-renderer").shadowRoot.querySelector("div:nth-child(3) > form-renderer").shadowRoot.querySelector("div > div.main-content > div.container > wc-container > wc-container:nth-child(3) > wc-container:nth-child(2) > wc-scroll-container > wc-container:nth-child(4) > wc-fractal").shadowRoot.querySelector("slot > wc-slot > wc-container > wc-container:nth-child(1) > wc-text").shadowRoot.querySelector("div").click()')
        time.sleep(10)
        # verify
        driver.execute_script('document.querySelector("body > app-root > app-main-layout > nz-layout > nz-layout > nz-content > div > app-hatis-page > div > hatis-renderer").shadowRoot.querySelector("div:nth-child(3) > form-renderer").shadowRoot.querySelector("div > div.main-content > div.container > wc-container > wc-container:nth-child(4) > wc-container:nth-child(1) > wc-container:nth-child(2) > wc-select").shadowRoot.querySelector("#container > select").value = 3')
        driver.execute_script('document.querySelector("body > app-root > app-main-layout > nz-layout > nz-layout > nz-content > div > app-hatis-page > div > hatis-renderer").shadowRoot.querySelector("div:nth-child(3) > form-renderer").shadowRoot.querySelector("div > div.main-content > div.container > wc-container > wc-container:nth-child(4) > wc-container:nth-child(1) > wc-container:nth-child(2) > wc-select").shadowRoot.querySelector("#container > select").dispatchEvent(new Event("change"))')
        # proceed
        driver.execute_script('document.querySelector("body > app-root > app-main-layout > nz-layout > nz-layout > nz-content > div > app-hatis-page > div > hatis-renderer").shadowRoot.querySelector("div:nth-child(3) > form-renderer").shadowRoot.querySelector("div > div.main-content > div.container > wc-container > wc-container:nth-child(4) > wc-container:nth-child(1) > wc-container:nth-child(3) > wc-button").shadowRoot.querySelector("button").click()')
        time.sleep(10)
        # comment
        driver.execute_script('document.querySelector("body > app-root > app-main-layout > nz-layout > nz-layout > nz-content > div > app-hatis-page > div > hatis-renderer").shadowRoot.querySelector("div.modal > div > div > hatis-renderer").shadowRoot.querySelector("div:nth-child(3) > form-renderer").shadowRoot.querySelector("div > div.main-content > div.container > wc-container > wc-container > wc-container:nth-child(2) > wc-textarea").shadowRoot.querySelector("#container > textarea").value = "verify"')
        driver.execute_script('document.querySelector("body > app-root > app-main-layout > nz-layout > nz-layout > nz-content > div > app-hatis-page > div > hatis-renderer").shadowRoot.querySelector("div.modal > div > div > hatis-renderer").shadowRoot.querySelector("div:nth-child(3) > form-renderer").shadowRoot.querySelector("div > div.main-content > div.container > wc-container > wc-container > wc-container:nth-child(2) > wc-textarea").shadowRoot.querySelector("#container > textarea").dispatchEvent(new Event("input"))')
        # add comment
        driver.execute_script('document.querySelector("body > app-root > app-main-layout > nz-layout > nz-layout > nz-content > div > app-hatis-page > div > hatis-renderer").shadowRoot.querySelector("div.modal > div > div > hatis-renderer").shadowRoot.querySelector("div:nth-child(3) > form-renderer").shadowRoot.querySelector("div > div.main-content > div.container > wc-container > wc-container > wc-container:nth-child(3) > wc-button").shadowRoot.querySelector("button").click()')
        time.sleep(5)
        # drnafter
        drnafter = driver.execute_script('return document.querySelector("body > app-root > app-main-layout > nz-layout > nz-layout > nz-content > div > app-hatis-page > div > hatis-renderer").shadowRoot.querySelector("div.modal > div > div > hatis-renderer").shadowRoot.querySelector("div:nth-child(3) > form-renderer").shadowRoot.querySelector("div > div.main-content > div.container > wc-container > wc-container > wc-container:nth-child(1) > wc-text:nth-child(1)").shadowRoot.querySelector("div").innerText.split(".")[1].split(" ")[6]')
        # okbutton
        driver.execute_script('document.querySelector("body > app-root > app-main-layout > nz-layout > nz-layout > nz-content > div > app-hatis-page > div > hatis-renderer").shadowRoot.querySelector("div.modal > div > div > hatis-renderer").shadowRoot.querySelector("div:nth-child(3) > form-renderer").shadowRoot.querySelector("div > div.main-content > div.container > wc-container > wc-container > wc-container:nth-child(2) > wc-button").shadowRoot.querySelector("button").click()')
        # documents
        driver.get('https://bits.drc.gov.bt/bits/47143f65-4b69-401e-8f60-667a26dfdc94')
        time.sleep(15)
        # enter drn
        driver.execute_script('document.querySelector("body > app-root > app-main-layout > nz-layout > nz-layout > nz-content > div > app-hatis-page > div > hatis-renderer").shadowRoot.querySelector("div:nth-child(3) > form-renderer").shadowRoot.querySelector("div > div.main-content > div.container > wc-container > wc-container:nth-child(2) > wc-container:nth-child(2) > wc-container:nth-child(2) > wc-container:nth-child(1) > wc-container:nth-child(2) > wc-input").shadowRoot.querySelector("#container > input").value ='+'"'+drnafter+'"'+'')
        driver.execute_script('document.querySelector("body > app-root > app-main-layout > nz-layout > nz-layout > nz-content > div > app-hatis-page > div > hatis-renderer").shadowRoot.querySelector("div:nth-child(3) > form-renderer").shadowRoot.querySelector("div > div.main-content > div.container > wc-container > wc-container:nth-child(2) > wc-container:nth-child(2) > wc-container:nth-child(2) > wc-container:nth-child(1) > wc-container:nth-child(2) > wc-input").shadowRoot.querySelector("#container > input").dispatchEvent(new Event("input"))')
        # search
        driver.execute_script('document.querySelector("body > app-root > app-main-layout > nz-layout > nz-layout > nz-content > div > app-hatis-page > div > hatis-renderer").shadowRoot.querySelector("div:nth-child(3) > form-renderer").shadowRoot.querySelector("div > div.main-content > div.container > wc-container > wc-container:nth-child(2) > wc-container:nth-child(3) > wc-container:nth-child(2) > wc-button").shadowRoot.querySelector("button").click()')
        time.sleep(5)
        # view
        driver.execute_script('document.querySelector("body > app-root > app-main-layout > nz-layout > nz-layout > nz-content > div > app-hatis-page > div > hatis-renderer").shadowRoot.querySelector("div:nth-child(3) > form-renderer").shadowRoot.querySelector("div > div.main-content > div.container > wc-container > wc-container:nth-child(3) > wc-container:nth-child(2) > wc-scroll-container > wc-container:nth-child(4) > wc-fractal").shadowRoot.querySelector("slot > wc-slot > wc-container > wc-container:nth-child(1) > wc-text").shadowRoot.querySelector("div").click()')
        time.sleep(10)
        # approve
        driver.execute_script('document.querySelector("body > app-root > app-main-layout > nz-layout > nz-layout > nz-content > div > app-hatis-page > div > hatis-renderer").shadowRoot.querySelector("div:nth-child(3) > form-renderer").shadowRoot.querySelector("div > div.main-content > div.container > wc-container > wc-container:nth-child(4) > wc-container:nth-child(1) > wc-container:nth-child(2) > wc-select").shadowRoot.querySelector("#container > select").value = 4')
        driver.execute_script('document.querySelector("body > app-root > app-main-layout > nz-layout > nz-layout > nz-content > div > app-hatis-page > div > hatis-renderer").shadowRoot.querySelector("div:nth-child(3) > form-renderer").shadowRoot.querySelector("div > div.main-content > div.container > wc-container > wc-container:nth-child(4) > wc-container:nth-child(1) > wc-container:nth-child(2) > wc-select").shadowRoot.querySelector("#container > select").dispatchEvent(new Event("change"))')
        # proceed
        driver.execute_script('document.querySelector("body > app-root > app-main-layout > nz-layout > nz-layout > nz-content > div > app-hatis-page > div > hatis-renderer").shadowRoot.querySelector("div:nth-child(3) > form-renderer").shadowRoot.querySelector("div > div.main-content > div.container > wc-container > wc-container:nth-child(4) > wc-container:nth-child(1) > wc-container:nth-child(3) > wc-button").shadowRoot.querySelector("button").click()')
        time.sleep(10)
        # tpn
        tpnafter = driver.execute_script('return document.querySelector("body > app-root > app-main-layout > nz-layout > nz-layout > nz-content > div > app-hatis-page > div > hatis-renderer").shadowRoot.querySelector("div.modal > div > div > hatis-renderer").shadowRoot.querySelector("div:nth-child(3) > form-renderer").shadowRoot.querySelector("div > div.main-content > div.container > wc-container > wc-container > wc-container:nth-child(1) > wc-container:nth-child(1) > wc-text").shadowRoot.querySelector("div").innerText.split(".")[1].split(" ")[6]')
        # okbutton
        driver.execute_script('document.querySelector("body > app-root > app-main-layout > nz-layout > nz-layout > nz-content > div > app-hatis-page > div > hatis-renderer").shadowRoot.querySelector("div.modal > div > div > hatis-renderer").shadowRoot.querySelector("div:nth-child(3) > form-renderer").shadowRoot.querySelector("div > div.main-content > div.container > wc-container > wc-container > wc-container:nth-child(2) > wc-button").shadowRoot.querySelector("button").click()')
        # taxpayer
        driver.get('https://bits.drc.gov.bt/bits/aee128cd-016f-4c8b-8049-f676dbbdd609')
        time.sleep(15)
        # enter tpn
        driver.execute_script('document.querySelector("body > app-root > app-main-layout > nz-layout > nz-layout > nz-content > div > app-hatis-page > div > hatis-renderer").shadowRoot.querySelector("div:nth-child(3) > form-renderer").shadowRoot.querySelector("div > div.main-content > div.container > wc-container > wc-container:nth-child(2) > wc-container:nth-child(1) > wc-container:nth-child(2) > wc-container:nth-child(2) > wc-container:nth-child(1) > wc-container:nth-child(2) > wc-input").shadowRoot.querySelector("#container > input").value = '+'"'+tpnafter+'"'+'')
        driver.execute_script('document.querySelector("body > app-root > app-main-layout > nz-layout > nz-layout > nz-content > div > app-hatis-page > div > hatis-renderer").shadowRoot.querySelector("div:nth-child(3) > form-renderer").shadowRoot.querySelector("div > div.main-content > div.container > wc-container > wc-container:nth-child(2) > wc-container:nth-child(1) > wc-container:nth-child(2) > wc-container:nth-child(2) > wc-container:nth-child(1) > wc-container:nth-child(2) > wc-input").shadowRoot.querySelector("#container > input").dispatchEvent(new Event("input"))')
        # search
        driver.execute_script('document.querySelector("body > app-root > app-main-layout > nz-layout > nz-layout > nz-content > div > app-hatis-page > div > hatis-renderer").shadowRoot.querySelector("div:nth-child(3) > form-renderer").shadowRoot.querySelector("div > div.main-content > div.container > wc-container > wc-container:nth-child(2) > wc-container:nth-child(1) > wc-container:nth-child(3) > wc-container:nth-child(1) > wc-button").shadowRoot.querySelector("button").click()')
        time.sleep(5)
        # view
        driver.execute_script('document.querySelector("body > app-root > app-main-layout > nz-layout > nz-layout > nz-content > div > app-hatis-page > div > hatis-renderer").shadowRoot.querySelector("div:nth-child(3) > form-renderer").shadowRoot.querySelector("div > div.main-content > div.container > wc-container > wc-container:nth-child(2) > wc-container:nth-child(2) > wc-container:nth-child(2) > wc-scroll-container > wc-fractal").shadowRoot.querySelector("slot > wc-slot > wc-container > wc-container:nth-child(1) > wc-container > wc-text").shadowRoot.querySelector("div").click()')
        time.sleep(15)
        # edit
        driver.execute_script('document.querySelector("body > app-root > app-main-layout > nz-layout > nz-layout > nz-content > div > app-hatis-page > div > hatis-renderer").shadowRoot.querySelector("div:nth-child(3) > form-renderer").shadowRoot.querySelector("div > div.main-content > div.container > wc-container > wc-container:nth-child(2) > wc-container:nth-child(1) > wc-container:nth-child(4) > wc-container:nth-child(2) > wc-container:nth-child(2) > wc-container > wc-button").shadowRoot.querySelector("button").click()')
        # get number
        num = driver.execute_script('return document.querySelector("body > app-root > app-main-layout > nz-layout > nz-layout > nz-content > div > app-hatis-page > div > hatis-renderer").shadowRoot.querySelector("div:nth-child(3) > form-renderer").shadowRoot.querySelector("div > div.main-content > div.container > wc-container > wc-container:nth-child(2) > wc-container:nth-child(4) > wc-container:nth-child(2) > wc-fractal").shadowRoot.querySelector("slot > wc-slot > wc-container:nth-child(1) > wc-container:nth-child(2) > wc-container > wc-container:nth-child(1) > wc-container:nth-child(2) > wc-container:nth-child(1) > wc-input").shadowRoot.querySelector("#container > input").value')
        number = str(num)
        # compare
        self.assertEqual(number,"17407438")
        
if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        report_name= "Agency_Test_Result",
        report_title= "Agency_Test_Result"
    ))
