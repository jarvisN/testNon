# Class Spectrometer

ถูกออกแบบมาเพื่อเชื่อมต่อกับเครื่องมือวัดสเปกตรัมผ่านทางการเชื่อมต่อแบบซีเรียล คลาสนี้มีเมธอดสำหรับส่งคำสั่ง, รับช่วงความยาวคลื่น, รับรหัสอุปกรณ์, หยุดอุปกรณ์, ตั้งค่าการเปิดรับแสงอัตโนมัติ, และเริ่มการทำงานของอุปกรณ์

## Set up

```python
spectrometer = Spectrometer(port='COM3', baudrate=921600)
```

- `port`: พอร์ต COM ที่เครื่องมือวัดสเปกตรัมเชื่อมต่อ (ค่าเริ่มต้นคือ `COM3`)
- `baudrate`: อัตราบอดสำหรับการเชื่อมต่อแบบซีเรียล (ค่าเริ่มต้นคือ `921600`)

## Methods

### `send_command(self, command_bytes)`
ส่งคำสั่งไปยังเครื่องมือวัดสเปกตรัมและรับคำตอบกลับ

```python
def send_command(self, command_bytes):
    self.ser.write(command_bytes)
    response = self.ser.read_until(b'\x0D\x0A')
    return response
```

- `command_bytes`: อาร์เรย์ของไบต์สำหรับคำสั่งที่จะส่ง

### `get_wavelength_range(self)`
ส่งคำสั่งเพื่อรับช่วงความยาวคลื่นของเครื่องมือวัดสเปกตรัม

```python
def get_wavelength_range(self):
    command_bytes = bytearray.fromhex('CC 01 09 00 00 0F E5 0D 0A')
    response = self.send_command(command_bytes)
    start_wavelength, end_wavelength = struct.unpack('<HH', response[7:11])
    print(f"Start Wavelength: {start_wavelength}, End Wavelength: {end_wavelength}")
    return start_wavelength, end_wavelength
```

### `get_device_id(self)`
ส่งคำสั่งเพื่อรับรหัสอุปกรณ์ของเครื่องมือวัดสเปกตรัม

```python
def get_device_id(self):
    command_bytes = bytearray.fromhex('CC 01 0A 00 00 08 10 EF 0D 0A')
    response = self.send_command(command_bytes)
    device_id = response[7:-3].decode('ascii')
    return f"Device: {device_id}"
```

### `stop_work(self)`
ส่งคำสั่งเพื่อหยุดการทำงานของเครื่องมือวัดสเปกตรัม

```python
def stop_work(self):
    command_bytes = bytearray.fromhex('CC 01 09 00 00 04 DA 0D 0A')
    self.send_command(command_bytes)
    print("STOP Done")
```

### `set_auto_exposure(self)`
ส่งคำสั่งเพื่อตั้งค่าการเปิด

รับแสงอัตโนมัติ

```python
def set_auto_exposure(self):
    command_bytes = bytearray.fromhex('CC 01 09 00 00 0B E1 0D 0A')
    response = self.send_command(command_bytes)
    if not response:
        raise Exception('No response from device')
    response_bytes = bytearray(response)
    if response_bytes[7] == 0x00:
        print('Auto exposure set successfully')
    elif response_bytes[7] == 0xFF:
        raise Exception('Failed to set auto exposure')
    else:
        raise Exception(f'Unexpected response: {response.hex()}')
```

### `run_start(self)`
ส่งคำสั่งเพื่อเริ่มการทำงานของเครื่องมือวัดสเปกตรัม

```python
def run_start(self):
    # Code for run_start here...
```

## Example 

```python
# สร้างอินสแตนซ์ของคลาส Spectrometer
spectrometer = Spectrometer()

# รับช่วงความยาวคลื่น
start_wavelength, end_wavelength = spectrometer.get_wavelength_range()

# รับรหัสอุปกรณ์
device_id = spectrometer.get_device_id()

# หยุดการทำงานของเครื่องมือวัดสเปกตรัม
spectrometer.stop_work()

# ตั้งค่าการเปิดรับแสงอัตโนมัติ
spectrometer.set_auto_exposure()

# เริ่มการทำงานของเครื่องมือวัดสเปกตรัม
result = spectrometer.run_start()
```


**Note** : เมธอดที่ขึ้นต้นด้วยเครื่องหมายขีดล่าง (`_`) มีไว้สำหรับใช้ภายในและไม่ได้เป็นส่วนหนึ่งของ API สาธารณะ


คุณสามารถเพิ่มหรือลดรายละเอียดของเอกสารนี้ตามที่คุณต้องการ และหากมีเมธอดอื่นๆ ในโค้ดที่คุณต้องการให้เอกสารนี้ครอบคลุม คุณก็สามารถเพิ่มเมธอดเหล่านั้นไปยังเอกสารได้เช่นกัน โปรดสังเกตว่าฉันได้ใส่เมธอด `run_start` เป็นตัวอย่างเท่านั้น คุณควรจะใส่โค้ดจริงสำหรับเมธอดนั้นแทนที่ข้อความ `# Code for run_start here...`.