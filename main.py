import gameoflife

if __name__ == '__main__':
    # You should not modify this part.

    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--width',
                       default='60',
                       help='input the width of the map')
    parser.add_argument('--height',
                        default='23',
                        help='input the height of the map')
    parser.add_argument('--pattern',
                        default='3',
                        help='input pattern')
    parser.add_argument('--generation',
                        default='20',
                        help='input generation')
    args = parser.parse_args()

    w = int(args.width)
    h = int(args.height)
    p = int(args.pattern)
    t = int(args.generation)

i=gameoflife.GameofLife(w,h)
i.initialize(p)
i.proceed(t)

