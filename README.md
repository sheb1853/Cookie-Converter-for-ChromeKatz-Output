# Cookie Converter for ChromeKatz Output

First of all, **huge congratulations** to the amazing creator of [ChromeKatz](https://github.com/Meckazin), a tool designed to extract cookies from Chrome's data stores.
---

## **About This Tool**

This script is designed to convert the output of **ChromeKatz** to a **JSON** format that can be directly imported into the **Cookie Editor** extension for Chrome. It processes extracted cookies and outputs a properly formatted JSON file for easy browser import.

---

## **Features**

- Converts ChromeKatz cookie output to JSON format.
- Supports importing JSON into Chrome's **Cookie Editor** extension.
- Handles cookies with properties like domain, path, secure flag, HttpOnly flag, expiration time, and value.

---

## **Usage**

### **Prerequisites**

- Python 3.x installed on your system.

### **Command Syntax**

```bash
python json-converter.py -file <input-cookie-file>

