def end_purchase():
        while True:
            try:  # Declines tracking consent
                driver.find_element_by_class_name("decline.btn.btn-primary").click()

                # Erasing the text field, replacing it with the desired quatity, and adding it to the shopping cart
                search = driver.find_element_by_class_name("form-control.quantity-select.quantity.quantity-input")
                search.send_keys(Keys.BACK_SPACE)
                time.sleep(0.2)
                search.send_keys(quantity)
                search.send_keys(Keys.RETURN)

                time.sleep(0.2)
                # Pressing the Add to Cart Button
                # Will need to add a condition in case this path doesn't work try another
                addToCart = driver.find_element_by_class_name("add-to-cart.btn.btn-primary")
                addToCart.send_keys(Keys.RETURN)
                time.sleep(0.2)
                # Takes you to the shopping cart for checkout
                driver.get("https://www.speer.com/cart")
                time.sleep(0.8)
                # Selects the State
                selectState = driver.find_element_by_id("TX").click()
                time.sleep(0.2)
                # Will need to add a condition in case this path doesn't work try another
                applyState = driver.find_element_by_class_name("btn.btn-primary.btn-block.shipping-restrictions")
                applyState.send_keys(Keys.RETURN)
                time.sleep(0.2)
                checkoutButton = driver.get(
                    "https://www.speer.com/on/demandware.store/Sites-VistaSpeer-Site/default/Checkout-Login")
                # checkoutButton.send_keys(Keys.RETURN)

                time.sleep(0.4)

                # Login as a returning customer
                emailLogin = driver.find_element_by_id("login-form-email")
                emailLogin.send_keys(userEmail)
                passwordLogin = driver.find_element_by_id("login-form-password")
                passwordLogin.send_keys(password)

                time.sleep(0.4)

                # Pressing the login button
                pressLogin = driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div[2]/div[2]/form/button")
                pressLogin.send_keys(Keys.RETURN)

                time.sleep(0.8)

                # #The next step is to get this to press the "NEXT: VALIDATE ADDRESS BUTTON" The below isn't working so far.
                validateAddress = driver.find_element_by_class_name("btn.btn-primary.btn-block.submit-shipping")
                validateAddress.send_keys(Keys.RETURN)

                time.sleep(1)

                enterEmail = driver.find_element_by_class_name("form-control.email")
                enterEmail.send_keys(userEmail)

                time.sleep(1)

                creditCardNumber = driver.find_element_by_class_name("form-control.cardNumber")
                creditCardNumber.send_keys(creditCard)

                driver.find_element_by_id(cardMonth).click()
                driver.find_element_by_id(cardYear).click()

                securityCode = driver.find_element_by_class_name("form-control.securityCode")
                securityCode.send_keys(cardSecurityCode)

                reviewOrder = driver.find_element_by_class_name("btn.btn-primary.btn-block.submit-payment")
                reviewOrder.send_keys(Keys.RETURN)

                time.sleep(1)

                # Clicking the age verification box
                driver.find_element_by_xpath(
                    "/html/body/div[2]/div[1]/div[4]/div[1]/div[6]/div[3]/div/label").click()

                # placeOrder = driver.find_element_by_class_name("btn.btn-primary.btn-block.place-order")
                # placeOrder.send_keys(Keys.RETURN)
            except Exception:
                continue
