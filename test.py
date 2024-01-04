sdk_mames = ["Umeng",
            "sharesdk",
            "Firebase",
            'yandex',
            "GA",
            "ad4screen",
            "jiubang",
            "Kissmetrics",
            "Mixpanel",
            "Heap",
            "GrowingIO",
            "Sensors",
            "Baidu",
            "Talkingdata",
            "Zhuge",
            "Amplitude",]


Result = {"Umeng":set(),
            "sharesdk":set(),
            "Firebase":set(),
            'yandex':set(),
            "GA":set(),
            "ad4screen":set(),
            "jiubang":set(),
            "Kissmetrics":set(),
            "Mixpanel":set(),
            "Heap":set(),
            "GrowingIO":set(),
            "Sensors":set(),
            "Baidu":set(),
            "Talkingdata":set(),
            "Zhuge":set(),
            "Amplitude":set()}
app_list = {name: set() for name in sdk_mames}
flag_list = {name: 0 for name in sdk_mames}

print(app_list)
print(flag_list)

