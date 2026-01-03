# The script of the game goes in this file.

# Function to resize
transform scale(ratio):
    zoom ratio

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define richel = Character("Richèl", color = "#f80")

# The game starts here.
label start:

label outside_no_slack:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene ums_outer_door at scale(2.0)

    "Du är framför ytterdörren av Uppsala Makerspace."

    "Du prövar dörren. Den är låst."

    "Vad vill du göra?"

    menu:

        "Använder Slack":

            "Du skapar en post på Slack, för att be om hjälp för att öppna dörren."

            jump outside_after_slack

        "Vänta":

            "Du väntar litegrann ..."

            jump outside_no_slack


label outside_after_slack:

    "En kille dyker upp"

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.
    show richel at scale(3.0), right

    # These display lines of dialogue.
    richel "Välkommen till Uppsala Makerspace! Jag öppnar dörren för dig!"

    "Killen öppnar dörren. Du går in."

    richel "Ha det så kul!"

    "Killen lämnar dig genast"

    hide richel

label hallway:

    scene ums_inner_door at scale(2.0)

    "Du är framför innerdörren av Uppsala Makerspace."

    "Du prövar dörren. Den är låst."

    "Vad vill du göra?"

    menu:

        "Använder Slack":

            "Bra! Du har klarat spelet!"

        "Vänta":

            "Du väntar litegrann ..."

            jump hallway
