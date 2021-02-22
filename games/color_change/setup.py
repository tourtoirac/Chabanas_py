def return_json_setup():
    json_setup={
        "games": [
            {
                "key1":{
                    "player_code":"player_code",
                    "guest_code":"guest_code",
                    "player_list":[],
                    "windows":{
                        "height":100,
                        "width":100,
                        "bg_color":"bdbdbd"
                    },
                    "bg_objects":[],
                    "unselectable":[],
                    "selectable":[],
                    "overlay":[],
                    "hands":[]
                }
            }
        ]
    }
    return(json_setup)