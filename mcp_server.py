"""MCP Server for Dynamic Time Warping Skill."""
import json
import sys
from client import DynamicTimeWarping

def main():
    for line in sys.stdin:
        if not line.strip():
            continue
        try:
            req = json.loads(line)
            req_id = req.get("id")
            method = req.get("method")
            params = req.get("params", {})

            if method == "tools/list":
                res = {
                    "jsonrpc": "2.0",
                    "id": req_id,
                    "result": {
                        "tools": [{
                            "name": "align_sequences_dtw",
                            "description": "Align temporal sequences and compute DTW distance",
                            "inputSchema": {
                                "type": "object",
                                "properties": {
                                    "seq1": {"type": "array", "items": {"type": "number"}},
                                    "seq2": {"type": "array", "items": {"type": "number"}}
                                },
                                "required": ["seq1", "seq2"]
                            }
                        }]
                    }
                }
            elif method == "tools/call":
                args = params.get("arguments", {})
                dist, path = DynamicTimeWarping.distance(args["seq1"], args["seq2"])
                res = {
                    "jsonrpc": "2.0",
                    "id": req_id,
                    "result": {"content": [{"type": "text", "text": json.dumps({"distance": dist, "path": path})}]}
                }
            else:
                res = {"jsonrpc": "2.0", "id": req_id, "error": {"code": -32601, "message": "Method not found"}}
            print(json.dumps(res), flush=True)
        except Exception as e:
            err = {"jsonrpc": "2.0", "id": None, "error": {"code": -32000, "message": str(e)}}
            print(json.dumps(err), flush=True)

if __name__ == "__main__":
    main()
