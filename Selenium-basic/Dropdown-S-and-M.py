from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


def getAttribute(element1):
    attrs = driver.execute_script("""
        let el = arguments[0];
        let obj = {};
        for (let attr of el.attributes) {
            obj[attr.name] = attr.value;
        }
        return obj;
    """, element1)

    return attrs


driver = webdriver.Firefox()
driver.maximize_window()

driver.get("https://omayo.blogspot.com/")

element = driver.find_element(By.CSS_SELECTOR, "select#drop1.combobox")
multielement = driver.find_element(By.CSS_SELECTOR, "select#multiselect1")

select = Select(element)
mutl = Select(multielement)

print("Single attributes:", getAttribute(element))
print("Is single select multiple?:", select.is_multiple)

select.select_by_index(1)

print("Multi attributes:", getAttribute(multielement))
print("Is multi select?:", mutl.is_multiple)


mutl.select_by_index(1)
mutl.select_by_index(2)


for option in mutl.all_selected_options:
    print("Selected:", option.text)

driver.quit()