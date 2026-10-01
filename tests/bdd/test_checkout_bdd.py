from playwright.sync_api import expect
from pytest_bdd import scenarios, when, then, parsers

scenarios("features/checkout.feature")


@when("the user starts checkout")
def start_checkout(cart_page):
    cart_page.checkout()


@when("the user submits valid checkout information")
def submit_valid_info(checkout_page, users):
    checkout_page.fill_info(**users["checkout_info"])


@when(parsers.re(r'the user submits checkout information with first name "(?P<first>.*)" last name "(?P<last>.*)" and postal code "(?P<postal>.*)"'))
def submit_info(checkout_page, first, last, postal):
    checkout_page.fill_info(first, last, postal)


@when("the user finishes the order")
def finish_order(checkout_page):
    checkout_page.finish()


@then(parsers.parse('the order confirmation says "{text}"'))
def confirmation_says(checkout_page, text):
    expect(checkout_page.complete_header).to_have_text(text)


@then(parsers.parse('the checkout error contains "{text}"'))
def checkout_error(checkout_page, text):
    expect(checkout_page.error).to_contain_text(text)
