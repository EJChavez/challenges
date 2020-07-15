is_magician = False
is_expert = False

#check if magician And expert: "you are a master magician"

#check if magician but not expert: "at least you're getting there"

#if you're not a magician "you need magic powers"

if is_magician and is_expert:
    print('you are a master magician')
elif is_magician and not is_expert:
    print("at least you're getting there")
elif not is_magician:
    print('you need magic powers')
else:
    print('what the hell are you doing here.')
