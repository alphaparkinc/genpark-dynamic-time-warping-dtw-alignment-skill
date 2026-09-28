import sys
import json
from client import DynamicTimeWarping

def handle_request(req):
    method = req.get("method")
    req_id = req.get("id")
    
    if method == "initialize":
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": {
                "protocolVersion": "2024-11-05",
                "capabilities": {"tools": {}},
                "serverInfo": {"name": "genpark-dynamic-time-warping-dtw-alignment-skill", "version": "1.0.0"}
            }
        }
    elif method == "tools/list":
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": {
                "tools": [
                    {
                        "name": "align_dtw_sequences",
                        "description": "Compute non-linear warping distance between two time-series sequences",
                        "inputSchema": {
                            "type": "object",
                            "properties": {
                                "series_a": {"type": "array", "items": {"type": "number"}},
                                "series_b": {"type": "array", "items": {"type": "number"}},
                                "window": {"type": "integer"}
                            },
                            "required": ["series_a", "series_b"]
                        }
                    }
                ]
            }
        }
    elif method == "tools/call":
        params = req.get("params", {})
        tool_name = params.get("name")
        args = params.get("arguments", {})
        
        if tool_name == "align_dtw_sequences":
            sa = args.get("series_a", [])
            sb = args.get("series_b", [])
            w = args.get("window")
            res = DynamicTimeWarping.compute_distance(sa, sb, window=w)
            return {
                "jsonrpc": "2.0",
                "id": req_id,
                "result": {
                    "content": [{"type": "text", "text": json.dumps(res)}]
                }
            }
    return {"jsonrpc": "2.0", "id": req_id, "error": {"code": -32601, "message": "Method not found"}}

def main():
    for line in sys.stdin:
        if not line.strip():
            continue
        try:
            req = json.loads(line)
            res = handle_request(req)
            sys.stdout.write(json.dumps(res) + "\n")
            sys.stdout.flush()
        except Exception as e:
            err = {"jsonrpc": "2.0", "id": None, "error": {"code": -32700, "message": str(e)}}
            sys.stdout.write(json.dumps(err) + "\n")
            sys.stdout.flush()

if __name__ == "__main__":
    main()
