=== RAPPORT K8S-AI-GUARDIAN ===
Généré le : 2026-03-23 20:17:20
Mode : LIVE

--- RAPPORT OBSERVATEUR ---
- [CRITICAL] Pod: oom-app-7c75f7d8c6-fj5kq | Namespace: default | Problème: CrashLoopBackOff | Restarts: 10 | Node: minikube-m02
- [CRITICAL] Pod: bad-image-app-694d895f68-qrns2 | Namespace: default | Problème: ErrImagePull | Restarts: 0 | Node: minikube-m02
- [CRITICAL] Pod: crash-loop-app-7f9c8c748d-27p4v | Namespace: default | Problème: Error | Restarts: 10 | Node: minikube
- [CRITICAL] Pod: crash-loop-app-7f9c8c748d-x4h49 | Namespace: default | Problème: Error | Restarts: 10 | Node: minikube-m02
- [WARNING] Pod: pending-pod | Namespace: default | Problème: Pending | Restarts: 0 | Node: None

AUCUNE ANOMALIE NODE — Tous les nodes sont sains

EVENEMENTS WARNING (7) :
- [Failed] Pod/bad-image-app-694d895f68-qrns2 | Namespace: default | Message: Failed to pull image "nginx:version-qui-nexiste-pas" : Error response from daemon: manifest for nginx: version-qui-nexiste-pas
- [Failed] Pod/bad-image-app-694d895f68-qrns2 | Namespace: default | Message: Error: ErrImagePull | Count: 5
- [Failed] Pod/bad-image-app-694d895f68-qrns2 | Namespace: default | Message: Error: ImagePullBackOff | Count: 109
- [BackOff] Pod/crash-loop-app-7f9c8c748d-27p4v | Namespace: default | Message: Back-off restarting failed container crash-loop-container in pod crash-loop-app-7f9c8c748d-27p4v_def | Count: 24
- [BackOff] Pod/crash-loop-app-7f9c8c748d-x4h49 | Namespace: default | Message: Back-off restarting failed container crash-loop-container in pod crash-loop-app-7f9c8c748d-x4h49_def | Count: 25
- [BackOff] Pod/oom-app-7c75f7d8c6-fj5kq | Namespace: default | Message: Back-off restarting failed container oom-container in pod oom-app-7c75f7d8c6-fj5kq_default(13a20cd7-
- [FailedScheduling] Pod/pending-pod | Namespace: default | Message: 0/2 nodes are available: 2 Insufficient cpu, 2 Insufficient memory. no new claims to deallocate, pre

--- DIAGNOSTIC ---
{'city': '??', 'report_date': '2023-10-04T15:00:00Z', 'weather': {'temperature': '22°C', 'humidity': '68%', 'pressure': '1012 hPa'}}

--- ACTIONS DE REMÉDIATION ---

[2026-03-23 20:17:09] ÉCHEC
  Pod        : bad-image-app-694d895f68-qrns2
  Problème   : ImagePullBackOff
  Action     : rollback deployment bad-image-app
  Résultat   : ERREUR: error: no rollout history found for deployment "bad-image-app"

[2026-03-23 20:17:11] SUCCÈS
  Pod        : crash-loop-app-7f9c8c748d-27p4v
  Problème   : CrashLoopBackOff
  Action     : rollout restart crash-loop-app
  Résultat   : deployment.apps/crash-loop-app restarted

[2026-03-23 20:17:14] SUCCÈS
  Pod        : crash-loop-app-7f9c8c748d-x4h49
  Problème   : CrashLoopBackOff
  Action     : rollout restart crash-loop-app
  Résultat   : deployment.apps/crash-loop-app restarted

[2026-03-23 20:17:16] SUCCÈS
  Pod        : oom-app-7c75f7d8c6-fj5kq
  Problème   : CrashLoopBackOff
  Action     : rollout restart oom-app
  Résultat   : deployment.apps/oom-app restarted

[2026-03-23 20:17:18] ÉCHEC
  Pod        : pending-pod
  Problème   : Pending
  Action     : escalade humaine
  Résultat   : Ressources insuffisantes sur le cluster. Action requise : augmenter les ressources du cluster ou réduire les requests du pod.
