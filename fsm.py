from graphviz import Digraph

def chatbot_diagram():

    dot = Digraph()

    dot.attr(rankdir="LR")

    dot.node("q0", "START")
    dot.node("q1", "LOGIN")
    dot.node("q2", "INPUT BUDGET")
    dot.node("q3", "INPUT KEBUTUHAN")
    dot.node("q4", "REKOMENDASI")
    dot.node("q5", "DETAIL")
    dot.node("q6", "CHECKOUT")
    dot.node("q7", "PEMBAYARAN")
    dot.node("q8", "LOGOUT")

    dot.edge("q0", "q1")
    dot.edge("q1", "q2")
    dot.edge("q2", "q3")
    dot.edge("q3", "q4")
    dot.edge("q4", "q5")
    dot.edge("q5", "q6")
    dot.edge("q6", "q7")
    dot.edge("q7", "q8")

    return dot