creature = 'xBBDBDCBCAABDxCAxCBBxDCxABCACCADCxABDDCDCBDAACxDADCBBCCABBAACBABxDxAxABBCBBCABBDCAxBBCxDxDBDCAxDBADDBAABDCxBCCABADDxADBDAxADxBDABCDCBCBBACCABBxCCDCBABADCDCDBDDBBBBDCDAABBCDBDAACACBADCBBxADAAAADDxBBAxBBDCBDACCCABCAABDCDxxADDBAxDBACDABAACBDDDCDDACBxAxBBCBCDCBDCBDCBDCxxDCDDBCACCACDCDAADCAxxCCCxCCDBBCCACCBxDDAAACDxDDCDxxCxDAADCCCBDBxAACCxCAxDCAABxAxCCCDDAAADxBAAAACBBxAAxAABADDDDAACCBADxBCDCADADBABDBDCxDBDCBDBAxxDCBxBCBCBDDBBDBCCDCCCACDxDDBDDCDCxBDCBADDDDBCCCAAAACDDCDDBDCDBxDxBDxADBBDCDCBDBDxABBxAxBDCBBBxCCABCAABCxBxBBAABxABACxDBxDDBACxCCAAABACAxAADxCAAAxABBDxCDCDBABCADADDCBAxABCADCCBCCAABDxBDAxCBxDCDDDBABAAACCAADBAACxCBDABBxDCDCBBxABBCxABDBABACBDxCxABxDACDDAACxBBCBADACCDCBDAADCCBDxACCDCCCCAxDDBDBBADCCCABDDDDAABCDDDAACBADxxCBBBBBCDABCABABADABACBAADCxBCDDBBCBBDDBBxDACDCDBxCxBABDDCBAADADAABCDDCBDBxDBxBDBBDDDAACxADDCDBBCABBCBDBDxCBBDxADxAxBDACCDBABDBCCCCxCADACDCxxCxBxxBCxBCACCBCCDBAxDxADBAACCADBxDCADBDBAxBAACCxACABDDxxDDCDCBDBABABCxCCBDDDCDCAABADDADDBDADBBCAABABBCBCDxCADxBBxCCBDCCDABBADDCDDADACCDABCCCDCCDAAAxCxDCDDCCACDBxAxBCADBDBABxADBxBDDDAABDDxDBDDxBCxBCCBxCBxDBCCADxBDABCADBxxDDABxxDAxABCABADBAxBABACxCxBCDBACBBDDDAxBxBxADACCBDBADCBCBDxBCxAABCABBBDDAAADCDCBCBBBBCBCDABBAADADCDDCDDCCCDDABBDxBBDDxBAxCCBDBBDCCBxxCBxCxxDCAxACBDDDDCxAACCBDxCxAADAABDBBCBDBABABCBADBAADBCCDAAACxxxCDDxBCCCCDBBCBCxAABDDxACADCDCDCBDxxBCDABACDDCDxACxBCAABCBCCCxDBBBCCADDABCDAABBCBBDDCDBDCADCCCABAxDxBCBBDCABCAADCCCBBABABDABDxCCCCAAAACBADBCCDCAADCCxxDCCxCDBDBDCDCBBCxABACDCCAAxxDCBACxBBCDBBxACxCBDxDBCDDDAAADBDCADxDxCAAACCDBCADxCBCDBBDDAADCCxBCBABDAACCBAACxAADCACDADDBADxCDDDDDBDxABCBBADACBDDxDDxACCBxxCACCxDAACAxDDDCAAxCACBCDDADCCxCBxBxBACADCBxBCDBDCCCBABADADABADAACAxACBxCBxAACxCACDCxCCCAAAAxBBDBDABCDCDACCDADAxCxCDADDCBBDDCABCBAxDDBDBDBCABDDBBDABCBDBDDBACADCADBAAACxCCADBxAxBCBCABDAAABCBBxCCCxBADCABCABCBCAxxBDBCDCACBCBCAADDCCADBDDCCABBADDBxDDAABCCCBABBACCACCDABCBBBBBAAADCBDDAABBBxAADADACBBDDDCBBCBDCDCABDBABDBCCAABCxDACDDCCBBADxABDxBAADBADCCDCDDAACCDCBDxBBAAxADDxBAxBCBCABBBDCADBxCABCACDBDDAxCAADACCCCxDABCBxxD'

potions = 0

for c in range(0, len(creature), 2):
    pair = creature[c:c+2]
    if not 'X' in pair:
        potions += 2
    print(pair)