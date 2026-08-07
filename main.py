from src.main import parse_args, main

if __name__ == "__main__":
    args = parse_args()
    main(dry_run=args.dry_run)
