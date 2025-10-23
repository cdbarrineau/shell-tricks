"""
    This does not seem to work...
"""

from pynput import keyboard


# The event listener will be running in this block
with keyboard.Events() as events:
    for event in events:
        if event.key == keyboard.Key.esc:
            break
        else:
            print('Received event {}'.format(event))
            
            
# def on_press(key, injected):
#     try:
#         print('alphanumeric key {} pressed; it was {}'.format(
#             key.char, 'faked' if injected else 'not faked'))
#     except AttributeError:
#         print('special key {} pressed'.format(
#             key))
    
# def on_release(key, injected):
#     print('{} released; it was {}'.format(
#         key, 'faked' if injected else 'not faked'))
#     if key == keyboard.Key.esc:
#         # Stop listener
#         return False

# with keyboard.Listener(
#         on_press=on_press) as listener:
#     try:
#         listener.join()
#     except Exception as e:
#         print('{} was pressed'.format(e.args[0]))
    
# # listener = keyboard.Listener(
# #     on_press=on_press,
# #     on_release=on_release
# #  )

# print ('Starting Listener....')
# # listener.start()

# i = input('Input Something...')

# # listener.join()

# print ('Stopping Listener.')