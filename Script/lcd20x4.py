from RPLCD.i2c import CharLCD

class Lcd20x4:
    def __init__(self, i2cAddress: int, column: int, row: int):
        self.i2cAddress = i2cAddress
        self.port       = 0x01
        self.columns    = column
        self.rows       = row
        self.dotSize    = 8

        self.init()


    def init(self):
        self._lcd = CharLCD(
            i2c_expander = 'PCF8574',
            address      = self.i2cAddress,
            port         = self.port,
            cols         = self.columns,
            rows         = self.rows,
            dotsize      = self.dotSize)
        self.clean()

    def clean(self):
        self._lcd.clear()


    def setLcdCursor(self, row: int, column: int):
        self._lcd.cursor_pos = (row, column)


    def write(self,
                 text    : str,
                 row     : int  = -1,
                 column  : int  = -1,
                 padding : bool = False,
                 center  : bool = False):

        # if only row is passrd but no column value
        if row != -1 and column == -1:
            column = 0

        # padding is only allowed when center option is false
        if padding and not center:
            pad = self.columns - len(text)
            text = text + (" " * pad)

        # center text
        if center:
            pad = self.columns - len(text)
            leftPad = pad // 2
            rightPad = pad - leftPad
            text = (" " * leftPad) + text + (" " * rightPad)

        if row != -1:
            self.setLcdCursor(row, column)

        self._lcd.write_string(text)


    def turnOffBacklight(self):
        self._lcd.backlight_enabled = False


    def turnOnBacklight(self):
        self._lcd.backlight_enabled = True
