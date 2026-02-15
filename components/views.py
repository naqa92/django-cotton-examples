from django.shortcuts import render

def index(request):

    context = {
        "title": "Bienvenue sur la page de test des composants Django !",
        "paragraph": "Lorem ipsum dolor sit, amet consectetur adipisicing elit. Facere officia similique optio eum aspernatur ut laudantium, veritatis nostrum, quo eaque vero iste quos quas. Consequatur non est omnis rem mollitia?",
        "options": [
            {"value": "", "label": "Sélectionnez une option..."},
            {"value": "web", "label": "🌐 Développement Web"},
            {"value": "mobile", "label": "📱 Applications Mobile"},
            {"value": "desktop", "label": "💻 Applications Desktop"},
            {"value": "ai", "label": "🤖 Intelligence Artificielle"},
            {"value": "blockchain", "label": "⛓️ Blockchain"},
            {"value": "iot", "label": "🌐 Internet des Objets"},
            {"value": "cybersec", "label": "🔒 Cybersécurité"},
            {"value": "data", "label": "📊 Science des Données"},
            {"value": "cloud", "label": "☁️ Cloud Computing"},
            {"value": "devops", "label": "🔧 DevOps"},
        ],
        "contact_options": [
            {"value": "", "label": "Type de contact..."},
            {"value": "support", "label": "🆘 Support technique"},
            {"value": "sales", "label": "💼 Équipe commerciale"},
            {"value": "partnership", "label": "🤝 Partenariats"},
            {"value": "feedback", "label": "💬 Commentaires"},
            {"value": "press", "label": "📰 Relations presse"},
        ],
        "priority_options": [
            {"value": "", "label": "Priorité..."},
            {"value": "low", "label": "🟢 Faible"},
            {"value": "medium", "label": "🟡 Moyenne"},
            {"value": "high", "label": "🟠 Élevée"},
            {"value": "critical", "label": "🔴 Critique"},
        ],
    }

    return render(request, "index.html", context)
