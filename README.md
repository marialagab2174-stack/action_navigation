# Challenge : Action Server Navigation (ROS 2) 📍

Ce projet implémente un **Action Server** sous ROS 2 Jazzy. Contrairement aux services classiques (requête/réponse), les actions sont conçues pour des processus asynchrones longs, offrant un suivi de progression (Feedback) et un résultat final.

## 🎯 Objectifs du Challenge
- Implémenter un serveur d'action utilisant l'interface `nav2_msgs/action/NavigateToPose`.
- Simuler un déplacement robotique avec calcul de distance restante.
- Envoyer des **feedbacks** périodiques au client pour monitorer la progression.

## ⚙️ Fonctionnement
Le serveur écoute sur l'action `navigate_to_target`. Une fois un objectif reçu :
1. Il entame une simulation de mouvement de 10 secondes.
2. Chaque seconde, il publie la distance restante (`distance_remaining`).
3. Il valide l'objectif une fois la destination "atteinte".

## 🛠 Installation & Build
```bash
cd ~/ros2_ws
colcon build --packages-select action_navigation
source install/setup.bash
```

## 🚀 Utilisation

### Lancer le Serveur d'Action
```bash
ros2 run action_navigation nav_server
```

### Envoyer un objectif (Client Terminal)
Ouvrez un autre terminal et envoyez une commande de navigation :
```bash
ros2 action send_goal /navigate_to_target nav2_msgs/action/NavigateToPose "{pose: {header: {frame_id: 'map'}}}" --feedback
```
*L'option `--feedback` vous permet de voir la distance diminuer en temps réel dans votre terminal.*

## 📝 Concepts Clés
- **Goal Service** : Gestion de l'acceptation ou du refus de l'objectif.
- **Feedback** : Publication de données intermédiaires (progression).
- **Result** : Notification de la fin de la tâche.

---
**Développeur :** Maria Lagab  
**Spécialité :** Robotique et Système Intelligent  
**Machine :** Dell Latitude 7400
