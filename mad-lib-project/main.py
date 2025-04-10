print("\n'Welcome to 'Mad Libs Game'\n")
print("Let’s get a little real... this one’s for your soul.\n")
print("---------------------------------------------")

# User Inputs
name = input("What's your name? :")
past_experience = input("Share a past experience you've been through and what you learned from it :")
current_struggle = input("What are you struggling with right now? :")
goal = input("What’s your goal? :")
motivation = input("What motivates you? :")
reminder_word = input("What word or thought keeps you going? :")
print("---------------------------------------------")

# Show Message
print("\n💬 A gentle reminder for you:\n")

story = f"""
{name}, do you remember when you faced {past_experience}
It seemed tough at that time, but that very moment turned out to be your greatest lesson and strength.
Right now, you're grappling with {current_struggle}, and it feels like you're at a crossroads. But deep inside, you know that this journey — just like the last one — will teach you something powerful. You’ve overcome so much before, and you'll rise above this challenge too.
Your goal, {goal}, is within your reach. Trust in your passion and resilience because it will undoubtedly lead you there.
Whenever you feel like giving up, take a moment to remember what drives you. {motivation} is your fuel — don’t let it fade.
And always keep this in mind: "{reminder_word}
The steps you take today are shaping your future, {name}."""

print("---------------------------------------------")
print("Keep moving forward. No matter how difficult it may seem, your time to shine is coming soon. 💙")
print(story)
