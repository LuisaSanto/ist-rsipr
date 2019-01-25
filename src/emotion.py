class Emotion:
    def __init__(self, robot):
        self.robot = robot
        self.emotion_decay_rate = 0.95
        self.emotion_spike_factor = 5
        self.emotions = {'happy': 0.0, 'sadness': 0.0, 'neutral': 1.0, 'anger': 0.0}
        self.active_emotion = 'neutral'
        self.last_emotions = []

    def get_current_emotion(self):
        return self.active_emotion

    def set_current_emotion(self, emotion):
        self.active_emotion = emotion

    def add_expression(self, str_input):
        if str_input is 'neutral':
            self.robot.emotions['neutral'] += 0.2
            self.robot.reevaluate()
            return

        if str_input in self.robot.emotions:
            if str_input in self.robot.last_emotions:
                self.robot.emotions[str_input] += 0.5

            self.robot.last_emotions.append(str_input)
            self.robot.last_emotions = self.robot.last_emotions[-5:]

        self.robot.reevaluate()

    def add_speech_sentiment(self, input_string):
        if input_string == 'positive':
            self.robot.emotions['happy'] += 0.3
            self.robot.emotions['sadness'] -= 0.2
            self.robot.emotions['anger'] -= 0.2

        else:
            self.robot.emotions['sadness'] += 0.2
            self.robot.emotions['anger'] += 0.2
            self.robot.emotions['happy'] -= 0.2

        self.reevaluate()

    def reevaluate(self):
        self.robot.emotions[self.robot.active_emotion] *= self.robot.emotion_decay_rate
        # If happy / sad or angry are close, go to neutral

        if abs(self.robot.emotions['happy'] - self.robot.emotions['sadness']) < 0.5 or abs(self.robot.emotions['happy'] - self.robot.emotions['anger']) < 0.5:
            new_max = 'neutral'

        else:
            new_max = max(self.robot.emotions, key=lambda v: self.robot.emotions[v])

        if self.robot.active_emotion != new_max:
            self.robot.emotions[new_max] += self.robot.emotion_spike_factor
            self.robot.active_emotion = new_max
