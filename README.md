# Challenge : Publisher Silencieux (Debugging) 🛠️

Ce projet est un exercice de débogage sous **ROS 2 Jazzy**. L'objectif était d'identifier et de corriger trois erreurs critiques dans un nœud Python qui empêchaient la publication correcte des messages sur le topic `/robot/status`.

## 🎯 Le Challenge
Le code initial contenait des erreurs de syntaxe et de logique courantes lors du développement avec `rclpy`. Ce dépôt contient la version corrigée et fonctionnelle.

### 🔍 Bugs Identifiés & Corrigés :
1.  **Inversion des arguments** : La méthode `create_publisher` nécessite le type de message (`String`) en premier argument, puis le nom du topic.
2.  **Instanciation de message** : Correction de l'instanciation de l'objet `String()` (parenthèses manquantes).
3.  **Appel de la méthode publish** : Passage correct de l'objet message à la fonction `self.pub.publish(msg)`.

## 🛠 Compilation et Test
```bash
# Compiler le package
cd ~/ros2_ws
colcon build --packages-select publisher_silencieux
source install/setup.bash

# Lancer le nœud
ros2 run publisher_silencieux status_node
```

## 🚀 Vérification du fonctionnement
Pour confirmer que le nœud n'est plus "silencieux", utilisez la commande suivante :
```bash
ros2 topic echo /robot/status
```
*Vous devriez voir le message "OK" s'afficher toutes les secondes.*

---
**Développeur :** Maria Lagab  
**Spécialité :** Robotique et Système Intelligent  
**Système :** Ubuntu 24.04 | Dell Latitude 7400
