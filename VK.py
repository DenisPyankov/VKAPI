import vk_api
import sys

with open("tok.txt", "r") as file:
    access_token = file.read().strip()

if len(sys.argv) < 2:
    print("Пожалуйста, укажите ID пользователя в качестве аргумента командной строки.")
    sys.exit(1)

user_id = sys.argv[1]

vk_session = vk_api.VkApi(token=access_token)

vk = vk_session.get_api()
user_info = vk.users.get(user_ids=user_id, fields="status")[0]

if "status" in user_info:
    print("Статус пользователя:")
    print(user_info["status"])
else:
    print("Статус пользователя не указан.")

friends = vk.friends.get(user_id=user_id)
if "items" in friends:
    print("Список друзей:")
    for friend_id in friends["items"]:
        friend_info = vk.users.get(user_ids=friend_id)[0]
        print(friend_info["first_name"], friend_info["last_name"])
else:
    print("Не удалось получить список друзей.")

albums = vk.photos.getAlbums(owner_id=user_id)
if "items" in albums:
    print("Названия фотоальбомов:")
    for album in albums["items"]:
        print(album["title"])
else:
    print("Не удалось получить названия фотоальбомов.")

video_albums = vk.video.getAlbums(owner_id=user_id)
if "items" in video_albums:
    print("Названия видеоальбомов:")
    for video_album in video_albums["items"]:
        print(video_album["title"])
else:
    print("Не удалось получить названия видеоальбомов.")

groups = vk.groups.get(user_id=user_id, extended=1)
if "items" in groups:
    print("Список групп:")
    for group in groups["items"]:
        print(group["name"])
else:
    print("Не удалось получить список групп.")

followers = vk.users.getFollowers(user_id=user_id)
if "items" in followers:
    print("Список подписчиков:")
    for follower_id in followers["items"]:
        follower_info = vk.users.get(user_ids=follower_id)[0]
        print(follower_info["first_name"], follower_info["last_name"])
else:
    print("Не удалось получить список подписчиков.")
