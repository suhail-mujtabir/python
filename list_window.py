from win32 import win32gui
def list_windows():
    def winEnumHandler( hwnd, ctx ):
        if win32gui.IsWindowVisible( hwnd ):
            print ( hex( hwnd ), win32gui.GetWindowText( hwnd ) )

    win32gui.EnumWindows( winEnumHandler, None )
list_windows()