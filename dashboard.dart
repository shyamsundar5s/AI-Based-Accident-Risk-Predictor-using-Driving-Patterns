import 'package:flutter/material.dart';

class DashboardScreen extends StatelessWidget {
  const DashboardScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Dashboard'),
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            const Text('Welcome to the AI Accident Risk Predictor!'),
            ElevatedButton(
              onPressed: () {
                // Navigate to Prediction Screen
              },
              child: const Text('Start Monitoring'),
            ),
          ],
        ),
      ),
    );
  }
}
