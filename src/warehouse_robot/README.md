# 🤖 Warehouse Robot - Stratégies Behavior Tree

## Scénario
Robot d'entrepôt qui doit:
1. Livrer des colis (20-30 min)
2. Répondre aux alarmes batterie faible
3. Respecter les horaires de recharge

## Solutions proposées

### 1. Livraison de colis
- **Stratégie**: Node SÉQUENCE (Sequence Node)
- **Pourquoi**: Étapes ordonnées comme une recette
- **Exemple**: Prendre → Porter → Livrer → Retourner

### 2. Urgence batterie
- **Stratégie**: Node RÉCUPÉRATION (Recovery Node)
- **Pourquoi**: Priorité absolue - sécurité
- **Exemple**: Arrêter tout → Aller charger → Attendre

### 3. Recharge programmée
- **Stratégie**: Node PARALLÈLE (Parallel Node)
- **Pourquoi**: Multi-tâches possible
- **Exemple**: Continuer livraison + Aller vers charge

### 4. Multiple stratégies?
- **Réponse**: OUI! Robot adaptatif
- **Chaque situation = stratégie appropriée**

## Test
```bash
ros2 run warehouse_robot robot_controller