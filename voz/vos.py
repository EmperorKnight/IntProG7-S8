import win32com.client

for i in range(1,5):
    j = 1
    while j < 5:
        text = f"i: {i}, j: {j}"
        engine = win32com.client.Dispatch("SAPI.SpVoice")
        print(text)
        engine.Speak(text)
        j += 1

# engine = win32com.client.Dispatch("SAPI.SpVoice")
# voices = engine.GetVoices()

# for i, voice in enumerate(voices):
#     print(f"{i}: {voice.GetDescription()}")

# voices = engine.GetVoices()
# engine.Voice = voices.Item(0)
# engine.rate = -2