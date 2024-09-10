followers = [
  {"name": "Tina", "following": True, "verified": True, "follows_you": False},
  {"name": "Klaus", "following": True, "verified": False, "follows_you": False},
  {"name": "Julia", "following": True, "verified": False, "follows_you": True},
  {"name": "Andrew", "following": True, "verified": False, "follows_you": False}
]

result = True
while result:
  for follower in followers:
    # Checks to see if follower is not verified AND not following the user
    if follower["follows_you"] == False and follower["verified"] == False:
      unfollow = input(follower["name"] + " " + "doesn't follow you, would you like to unfollow them? (y/n): ")
      if unfollow == "y":
        print(follower["name"] + " " + "has been unfollowed")
        # Removes person who is unfollowing
        followers.remove(follower)
        # Shows updated dict
        print(followers)
      elif unfollow == "n":
        print("You are still following" + " " + follower["name"])
        print(followers)
        result = False



