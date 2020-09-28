from random import choice
print("Welcome to Rocket League Expirence, where I, your personal bot will guide you on how to be better!")
print("Ask about some technical skills within the game and I'll explain how to preform said action or to get better at it.")
print("Some requests include: arial, half-flip, rotations, prediction, and goalie")
def get_bot_response(user_response):
    arial_responses = ["jump and pull the car back then boost", "try air-rolling to twist and make faster adjustments", "angle the front of the car towards where you want to go", "conserve boost to travel longer distances (tap boost)"]
    flip_responses = ["jump and flip backwards and then cancel the flip halfway by pulling forward", "use this when in need to quickly head back to net", "make sure to air-roll when you backflip", "usefull to make quick transitions and build speed"]
    rotations_responses = ["if both teammates up, stay back for defense", "if a teammate is going up the side of the field, be ready for the cross", "after you make your challenge against opponent, rotate back field", "if low boost, rotate back and let your team know"]
    prediction_responses = ["if opponent is farther away from the ball then you, go", "pay attention to the angle of which the opponent is going to hit the ball from to see which way they'll hit it", "if opponent is up before you for an arial, don't jump for it", "check which way the opponent goalie's car is facing to hit it in a spot harder for them to reach"]
    goalie_responses = ["look up shadow defense and study it", "always try and jump up to block no matter what", "notice when the ball is going to hit post and not go in", "do not hesitate"]
    if user_response.upper() == "ARIAL":
        return choice(arial_responses)
    elif user_response.upper() == "HALF-FLIP":
        return choice(flip_responses)
    elif user_response.upper() == "ROTATIONS":
        return choice(rotations_responses)
    elif user_response.upper() == "PREDICTION":
        return choice(prediction_responses)
    elif user_response.upper() == "GOALIE":
        return choice(goalie_responses)
    else:
        return "i don't have any info on that right now sorry. try another out or say done to end."
    
while True:
    user_response = input("Try any of the 5 options (arial, half-flip, rotations, prediction, goalie)")
    if user_response.upper() == "DONE":
        break
    bot_response = get_bot_response(user_response)
    print(bot_response)