from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    devices = p.devices
    print(devices)
