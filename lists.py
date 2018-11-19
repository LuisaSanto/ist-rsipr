import cozmo

quit_cmds = ["b", "back", "q", "quit"]
exit_cmds = ["e", "exit"]
clear_cmds = ["c", "clear"]

# Lists of animations to randomly pull from
angry_anims = [cozmo.anim._AnimTrigger(name='DriveStartAngry', id=39),
               cozmo.anim._AnimTrigger(name='DriveEndAngry', id=33),
               cozmo.anim._AnimTrigger(name='DriveLoopAngry', id=36),
               cozmo.anim._AnimTrigger(name='FrustratedByFailure', id=57),
               cozmo.anim._AnimTrigger(name='FrustratedByFailureMajor', id=58),
               cozmo.anim._AnimTrigger(name='KnockOverFailure', id=82),
               cozmo.anim._AnimTrigger(name='MajorFail', id=89),
               cozmo.anim._AnimTrigger(name='PounceFail', id=162),
               cozmo.anim._AnimTrigger(name='RequestGameDrivingFail', id=183),
               cozmo.anim._AnimTrigger(name='RequestGamePickupFail', id=208),
               cozmo.anim._AnimTrigger(name='CubePounceLoseSession', id=23),
               cozmo.anim._AnimTrigger(name='RequestGameDrivingFail', id=183),
               cozmo.anim._AnimTrigger(name='CubePounceLoseRound', id=22),
               cozmo.anim._AnimTrigger(name='CantHandleTallStack', id=8)
               ]

sad_anims = [cozmo.anim._AnimTrigger(name='RequestGameKeepAwayDeny0', id=186),
             cozmo.anim._AnimTrigger(name='RequestGameKeepAwayDeny1', id=187),
             cozmo.anim._AnimTrigger(name='CubeMovedUpset', id=13)
             ]

happy_anims = [cozmo.anim._AnimTrigger(name='BuildPyramidSuccess', id=7),
               cozmo.anim._AnimTrigger(name='CubePounceFake', id=14),
               cozmo.anim._AnimTrigger(name='CubePounceWinHand', id=26),
               cozmo.anim._AnimTrigger(name='CubePounceWinRound', id=27),
               cozmo.anim._AnimTrigger(name='CubePounceWinSession', id=28),
               cozmo.anim._AnimTrigger(name='KnockOverSuccess', id=86),
               cozmo.anim._AnimTrigger(name='MajorWin', id=90),
               cozmo.anim._AnimTrigger(name='OnLearnedPlayerName', id=106),
               cozmo.anim._AnimTrigger(name='OnSpeedtapGameCozmoWinLowIntensity', id=120),
               cozmo.anim._AnimTrigger(name='OnSpeedtapGameCozmoWinHighIntensity', id=119),
               cozmo.anim._AnimTrigger(name='OnSpeedtapRoundCozmoWinHighIntensity', id=127),
               cozmo.anim._AnimTrigger(name='OnSpeedtapRoundCozmoWinLowIntensity', id=128),
               cozmo.anim._AnimTrigger(name='PounceSuccess', id=166),
               cozmo.anim._AnimTrigger(name='RollBlockSuccess', id=227)
               ]

neutral_anims = [cozmo.anim._AnimTrigger(name='NeutralFace', id=101),
                 cozmo.anim._AnimTrigger(name='NothingToDoBoredIdle', id=103),
                 cozmo.anim._AnimTrigger(name='OnboardingIdle', id=143)
                 ]
