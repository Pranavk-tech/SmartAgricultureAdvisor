def explain_crop(N,P,K,temp,humidity,ph,rainfall):

    reasons=[]

    if N>50:
        reasons.append(
        "✔ Nitrogen level suitable"
        )

    if P>40:
        reasons.append(
        "✔ Phosphorus level suitable"
        )

    if K>40:
        reasons.append(
        "✔ Potassium level suitable"
        )

    if 20<=temp<=35:

        reasons.append(
        "✔ Temperature ideal for crop growth"
        )

    if humidity>60:

        reasons.append(
        "✔ Humidity favorable"
        )

    if 5<=ph<=8:

        reasons.append(
        "✔ Soil pH suitable"
        )

    if rainfall>100:

        reasons.append(
        "✔ Rainfall level adequate"
        )

    return reasons