import time
from alarmdecoder import AlarmDecoder
from alarmdecoder.devices import USBDevice

def main():
    """
    Example application that prints messages from the panel to the terminal.
    """
    try:
        # Retrieve the first USB device
        device = AlarmDecoder(USBDevice.find())

        # Set up an event handler and open the device
        device.on_message += handle_message
        with device.open():
            while True:
                time.sleep(1)

    except Exception, ex:
        print 'Exception:', ex

def handle_message(sender, *args, **kwargs):
    """
    Handles message events from the AlarmDecoder.
    """
    msg = kwargs['message']

    print sender, msg.raw

if __name__ == '__main__':
    main()
