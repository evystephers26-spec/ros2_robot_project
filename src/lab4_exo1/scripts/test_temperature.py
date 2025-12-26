#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# pyright: reportMissingImports=false
# type: ignore
print("=" * 60)
print("🧪 TEST: Message TemperatureSensor - Lab4_Exo1")
print("=" * 60)

try:
    # Importe le message
    from lab4_exo1.msg import TemperatureSensor
    from std_msgs.msg import Header
    
    print("✅ 1. IMPORT RÉUSSI")
    print(f"   - Module: lab4_exo1")
    print(f"   - Message: TemperatureSensor")
    
    # Crée un message de test
    print("\n✅ 2. CRÉATION DU MESSAGE")
    msg = TemperatureSensor()
    
    # Configure le header
    msg.header = Header()
    msg.header.stamp.sec = 1234567890
    msg.header.stamp.nanosec = 987654321
    msg.header.frame_id = "temperature_sensor_frame"
    
    # Configure les données du capteur
    msg.sensor_id = "TEMP_SENSOR_001"
    msg.temperature = 23.7
    msg.humidity = 68.5
    msg.pressure = 101325.0
    msg.is_operational = True
    
    # Affiche les valeurs
    print("\n✅ 3. DONNÉES DU CAPTEUR")
    print(f"   - ID Capteur: {msg.sensor_id}")
    print(f"   - Température: {msg.temperature} °C")
    print(f"   - Humidité: {msg.humidity} %")
    print(f"   - Pression: {msg.pressure} Pa")
    print(f"   - Statut: {'OPÉRATIONNEL' if msg.is_operational else 'EN PANNE'}")
    
    # Test de modification
    print("\n✅ 4. TEST DE MODIFICATION")
    msg.temperature = 25.3
    msg.humidity = 72.0
    print(f"   - Nouvelle température: {msg.temperature} °C")
    print(f"   - Nouvelle humidité: {msg.humidity} %")
    
    print("\n" + "=" * 60)
    print("🎉 TEST RÉUSSI ! Message TemperatureSensor fonctionnel")
    print("=" * 60)
    
except ImportError as e:
    print(f"\n❌ ERREUR D'IMPORT: {e}")
    print("\n⚠️  SOLUTION:")
    print("   1. Ouvre un terminal")
    print("   2. cd ~/ros2_ws")
    print("   3. source install/setup.bash")
    print("   4. Relance ce script")
    
except Exception as e:
    print(f"\n❌ AUTRE ERREUR: {e}")

print("\n📋 Résumé:")
print("   - Message créé: ✅ TemperatureSensor.msg")
print("   - Champs: header, sensor_id, temperature, humidity, pressure, is_operational")
print("   - Type: ROS2 Custom Message")
print("   - Package: lab4_exo1")