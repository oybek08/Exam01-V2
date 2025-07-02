def matnli_baho(ball):
    if 90 <= ball <= 100:
        return "Ajoyib!"
    elif 80 <= ball <= 89:
        return "Zo'r!"
    elif 70 <= ball <= 79:
        return "Yaxshi!"
    elif 60 <= ball <= 69:
        return "Qoniqarli"
    elif 0 <= ball <= 59:
        return "Past baho"
    else:
        return "Notogri ball"

print(matnli_baho(91))